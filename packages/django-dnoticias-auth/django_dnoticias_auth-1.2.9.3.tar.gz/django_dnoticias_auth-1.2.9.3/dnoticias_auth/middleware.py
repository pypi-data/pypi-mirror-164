import logging
from re import Pattern
import time
from requests.exceptions import HTTPError
from urllib.parse import quote, urlencode

from django.http import HttpResponseRedirect, HttpRequest, JsonResponse

from dnoticias_auth.redis import KeycloakSessionStorage
from django.utils.module_loading import import_string
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import cached_property
from django.contrib.auth import BACKEND_SESSION_KEY
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib import auth
from django.urls import reverse


import requests
from mozilla_django_oidc.utils import absolutify, add_state_and_nonce_to_session
from mozilla_django_oidc.middleware import SessionRefresh as SessionRefreshOIDC
from dnoticias_services.authentication.keycloak import get_user_keycloak_info
from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from mozilla_django_oidc.utils import absolutify

from .utils import generate_oidc_cookies, get_cookie_equivalency, get_cookie_configuration
from .backends import ExtraClaimsOIDCAuthenticationBackend

User = get_user_model()
logger = logging.getLogger(__name__)


class BaseAuthMiddleware:
    @cached_property
    def exempt_url_patterns(self):
        exempt_patterns = set()

        for url_pattern in settings.AUTH_EXEMPT_URLS:
            if isinstance(url_pattern, Pattern):
                exempt_patterns.add(url_pattern)

        return exempt_patterns

    @cached_property
    def exempt_session_url_patterns(self):
        exempt_patterns = set()
        patterns = getattr(settings, "SESSION_CHECK_EXEMPT_URLS", [])

        for url_pattern in patterns:
            if isinstance(url_pattern, Pattern):
                exempt_patterns.add(url_pattern)

        return exempt_patterns 

    def _is_processable(self, request):
        pass


class SessionRefresh(SessionRefreshOIDC):
    def is_refreshable_url(self, request: HttpRequest) -> bool:
        """Takes a request and returns whether it triggers a refresh examination

        :param request:
        :returns: boolean
        """
        # Do not attempt to refresh the session if the OIDC backend is not used
        backend_session = request.session.get(BACKEND_SESSION_KEY)
        is_oidc_enabled = True
        if backend_session:
            auth_backend = import_string(backend_session)
            is_oidc_enabled = issubclass(auth_backend, OIDCAuthenticationBackend)

        return (
            request.method == 'GET' and
            not any(pat.match(request.path) for pat in self.exempt_url_patterns) and
            request.user.is_authenticated and
            is_oidc_enabled and
            request.path not in self.exempt_urls
        )

    def process_request(self, request):
        if not self.is_refreshable_url(request):
            logger.debug('request is not refreshable!!')
            return

        keycloak_storage = KeycloakSessionStorage(request.session.get('keycloak_session_id'))
        keycloak_session = keycloak_storage.load()
        keycloak_payload = keycloak_session.get('payload', {})

        session_token_expiration = request.session.get('oidc_id_token_expiration', 0)
        keycloak_token_expiration = keycloak_payload.get('oidc_id_token_expiration', 0)

        # This will use the keycloak token expiration saved in redis session instead of the
        # one saved in django session. This is because we need to refresh the keycloak token
        # for all django sessions instead of just one.
        expiration = keycloak_token_expiration or session_token_expiration
        now = time.time()

        if expiration > now:
            if session_token_expiration and keycloak_token_expiration:
                if keycloak_token_expiration > session_token_expiration:
                    logger.debug("Session token is expired, refreshing with keycloak...")
                    request.session['oidc_id_token_expiration'] = keycloak_token_expiration
                    request.session.modified = True

            # The id_token is still valid, so we don't have to do anything.
            logger.debug('id token is still valid (%s > %s)', expiration, now)
            return

        logger.debug('id token has expired')
        # The id_token has expired, so we have to re-authenticate silently.
        auth_url = self.OIDC_OP_AUTHORIZATION_ENDPOINT
        client_id = self.OIDC_RP_CLIENT_ID
        state = get_random_string(self.OIDC_STATE_SIZE)

        # Build the parameters as if we were doing a real auth handoff, except
        # we also include prompt=none.
        params = {
            'response_type': 'code',
            'client_id': client_id,
            'redirect_uri': absolutify(
                request,
                reverse(self.OIDC_AUTHENTICATION_CALLBACK_URL)
            ),
            'state': state,
            'scope': self.OIDC_RP_SCOPES,
            'prompt': 'none',
        }

        params.update(self.get_settings('OIDC_AUTH_REQUEST_EXTRA_PARAMS', {}))

        if self.OIDC_USE_NONCE:
            nonce = get_random_string(self.OIDC_NONCE_SIZE)
            params.update({
                'nonce': nonce
            })

        add_state_and_nonce_to_session(request, state, params)

        request.session['oidc_login_next'] = request.get_full_path()

        query = urlencode(params, quote_via=quote)
        redirect_url = '{url}?{query}'.format(url=auth_url, query=query)
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Almost all XHR request handling in client-side code struggles
            # with redirects since redirecting to a page where the user
            # is supposed to do something is extremely unlikely to work
            # in an XHR request. Make a special response for these kinds
            # of requests.
            # The use of 403 Forbidden is to match the fact that this
            # middleware doesn't really want the user in if they don't
            # refresh their session.
            response = JsonResponse({'refresh_url': redirect_url}, status=403)
            response['refresh_url'] = redirect_url
            return response
        return HttpResponseRedirect(redirect_url)


class LoginMiddleware(BaseAuthMiddleware, MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def _login_user(
        self,
        session_payload: dict,
        payload: dict,
        request: HttpRequest
    ):
        """Ge get or create the user and then proceed to log in

        :param access_token: The access token
        :param id_token: The id token
        :param payload: The payload used to get the token
        :param request: The request
        """
        UserModel = ExtraClaimsOIDCAuthenticationBackend()
        user = None

        access_token = session_payload.get('oidc_access_token')
        id_token = session_payload.get('oidc_id_token')
        token_expiration = session_payload.get("oidc_id_token_expiration")
        keycloak_session_id = session_payload.get("keycloak_session_id")

        try:
            user = UserModel.get_or_create_user(access_token, id_token, payload)
        except HTTPError as e:
            logger.debug("An HTTP error ocurred: {}".format(e))
        except:
            logger.exception("An exception has been ocurred on _login_user")

        if user:
            user.backend = "dnoticias_auth.backends.ExtraClaimsOIDCAuthenticationBackend"
            auth.login(request, user)

            request.session["oidc_access_token"] = access_token
            request.session["oidc_id_token"] = id_token
            request.session["oidc_id_token_expiration"] = token_expiration
            request.session["keycloak_session_id"] = keycloak_session_id
            request.session.save()

    def _is_processable(self, request):
        return (
            not any(pat.match(request.path) for pat in self.exempt_url_patterns) and
            not request.user.is_authenticated
        )

    def process_request(self, request):
        if not self._is_processable(request):
            return

        keycloak_session_id = request.COOKIES.get(get_cookie_equivalency("keycloak_session_id"))

        if not keycloak_session_id:
            return

        keycloak_session = KeycloakSessionStorage(keycloak_session_id, ".")
        main_session_data = keycloak_session.load()
        session_payload = main_session_data.get("payload")

        if not all([
            session_payload.get('oidc_id_token_expiration'),
            session_payload.get('oidc_access_token'),
            session_payload.get('oidc_id_token')
        ]):
            return

        # Token payload that is used in OIDC to get (or refresh) an user token
        token_payload = {
            'client_id': settings.OIDC_RP_CLIENT_ID,
            'client_secret': settings.OIDC_RP_CLIENT_SECRET,
            'grant_type': 'authorization_code',
            'code': None,
            'redirect_uri': absolutify(
                request,
                ''
            ),
        }

        self._login_user(
            session_payload,
            token_payload,
            request
        )

        return


class TokenMiddleware(BaseAuthMiddleware, MiddlewareMixin):
    """Just generates the cookie if the user is logged in"""
    def __init__(self, get_response):
        self.get_response = get_response

    def _is_processable(self, request):
        return (
            not any(pat.match(request.path) for pat in self.exempt_url_patterns) and
            request.user.is_authenticated
        )

    def _can_check_dcs_session(self, request):
        """Check if the request requires to check the sessionid on dcs
        
        :param request: httpRequest
        ...
        :return: True if the request if processable and the function proceeds to check the ssid
        """
        return (
            not any(pat.match(request.path) for pat in self.exempt_url_patterns)\
            and not any(pat.match(request.path) for pat in self.exempt_session_url_patterns)\
            and not request.user.is_authenticated\
            and request.COOKIES.get("sessionid")
        )

    def __is_user_migrated(self, email: str) -> bool:
        """Check on keycloak if the user has been migrated
        :param email: The user email that we will verify if has been migrated
        ...
        :return: True if the user has been migrated
        """
        user_info = get_user_keycloak_info(email)
        return bool(user_info.get("attributes", {}).get("user_migrated", False))

    def check_dcs_cookies(self, request, http_response):
        """Check the dcs cookies and redirects to password reset view
        
        :param request: httpRequest
        :param http_response: httpResponse
        ...
        :return: httpResponse
        """
        cookies = request.COOKIES
        session_id = cookies.get("sessionid")
        has_dcs_session_api = getattr(settings, "DCS_SESSION_MIGRATE_API_URL", False)

        # If we dont have a session_id cookie, we just return the initial response
        if not session_id or not has_dcs_session_api:
            return http_response

        dcs_session_api = getattr(settings, "DCS_SESSION_MIGRATE_API_URL")
        # We ask to the DCS the email associated to that session_id. This returns an email if the
        # sessionid is not anon, the user does not have @dnoticias.pt in his email and is not part
        # of the staff or superuser.
        response = requests.post(dcs_session_api, {"session_id": session_id})
        body = response.json()
        logger.debug("[DCS Session] Returned %s", body)

        if response.status_code == 200:
            if not body.get("error"):
                # Gets the email from body
                email = body.get("email")

                if not self.__is_user_migrated(email):
                    # We make an HttpResponseRedirect to the change password view
                    http_response = HttpResponseRedirect(reverse("password-recovery"))

                    request.session["migration_email"] = email
                    request.session["migration_next_url"] = request.build_absolute_uri()
                    request.session.save()

                # Deletes the sessionid cookie
                extra_data = get_cookie_configuration()
                extra_data.pop('expires')
                extra_data.pop('secure')
                extra_data.pop('httponly')
                http_response.delete_cookie('sessionid', **extra_data)

        return http_response

    def process_response(self, request, response):
        if self._can_check_dcs_session(request):
            response = self.check_dcs_cookies(request, response)

        # If the user is logged in then we set the cookies, else we delete it
        if self._is_processable(request):
            response = generate_oidc_cookies(request.session, response)

        return response
