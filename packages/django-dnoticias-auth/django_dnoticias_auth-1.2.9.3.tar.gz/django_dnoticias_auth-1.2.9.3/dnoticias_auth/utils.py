import logging
from datetime import datetime, timedelta
from typing import Optional, Union

from django.http import HttpResponse
from django.conf import settings

from .redis import KeycloakSessionStorage, GenericSessionStorage

logger = logging.getLogger(__name__)


def get_cookie_equivalency(
    name: Optional[str] = None,
    all_names: Optional[bool] = False
) -> Union[dict, str]:
    """Returns the cookie equivalency for the given name

    :param name: The name of the cookie
    :param all_names: If True, returns all the cookie equivalencies
    :return: The cookie equivalency or a dict with all the equivalencies
    :rtype: Union[dict, str]
    """
    EQUIVALENCY = {
        'oidc_login_next': 'dn_oln',
        'keycloak_session_id': 'dn_ksi',
        'user_context_used': 'dn_ucu',
    }

    return EQUIVALENCY.get(name) if not all_names else EQUIVALENCY


def get_cookie_configuration() -> dict:
    """Return the cookie configuration

    :return: The cookie configuration
    :rtype: dict
    """
    expiration_datetime = \
            datetime.now() + timedelta(minutes=settings.AUTH_COOKIE_EXPIRATION_MINUTES)
    expires = expiration_datetime.strftime("%a, %d-%b-%Y %H:%M:%S GMT")

    return {
        'expires': expires,
        'domain': settings.AUTH_COOKIE_DOMAIN,
        'secure': settings.AUTH_COOKIE_SECURE,
        'httponly': settings.AUTH_COOKIE_HTTPONLY,
        'samesite': 'Strict'
    }


def generate_oidc_cookies(session: dict, response: HttpResponse) -> HttpResponse:
    """Generates all the cookies needed on another clients to process the user

    :param session: The session data
    :param response: The response object
    :return: The response object
    :rtype: HttpResponse
    """
    # This script only works if we save the access token in session
    if settings.OIDC_STORE_ACCESS_TOKEN:
        keycloak_session_id = session.get('keycloak_session_id', {})
        oidc_login_next = session.get('oidc_login_next', '')

        # We need these tree variables to login, if at least one is None or empty, then return
        if not keycloak_session_id:
            logger.debug("No valid keycloak_session_id, returning default response")
            return response

        # Extra kwargs used in set_cookie
        extra_data = get_cookie_configuration()

        # Setting the cookies...
        response.set_cookie(
            get_cookie_equivalency('oidc_login_next'),
            oidc_login_next,
            **extra_data
        )

        if keycloak_session_id:
            response.set_cookie(
                get_cookie_equivalency('keycloak_session_id'),
                keycloak_session_id,
                **extra_data
            )

    return response


def delete_user_sessions(keycloak_session_id: str) -> None:
    """Deletes all the user sessions for this keycloak_session_id stored in redis

    :param keycloak_session_id: The keycloak_session_id
    :return: None 
    """
    try:
        keycloak_session = KeycloakSessionStorage(keycloak_session_id, ".")
        session_data = keycloak_session.load()
        django_sessions = session_data.get("sessions", "")
        django_sessions = django_sessions.split(',') if django_sessions else []

        for session in django_sessions:
            logger.debug("Deleting django session: %s", session)
            django_session = GenericSessionStorage(f"{settings.SESSION_REDIS_PREFIX}:{session}")
            django_session.delete()

        keycloak_session.delete()
    except:
        logger.exception("Failed to delete sessions using keycloak session %s", keycloak_session_id)
