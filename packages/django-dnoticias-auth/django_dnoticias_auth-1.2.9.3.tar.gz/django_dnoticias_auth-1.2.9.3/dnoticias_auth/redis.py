
import logging
import redis
import json
from typing import Optional, Union

from django.utils.encoding import force_str
from django.conf import settings

from redis_sessions.session import RedisServer

from dnoticias_auth.exceptions import InvalidSessionParameters

logger = logging.getLogger(__name__)


class KeycloakSessionStorage:
    REDIS_PREFIX = settings.DJANGO_KEYCLOAK_ASSOC_REDIS

    def __init__(self, keycloak_session_id: str, django_session_id: Optional[str] = None):
        self.server = RedisServer(None).get()
        self.keycloak_session_id = keycloak_session_id
        self.django_session_id = django_session_id

    def load(self) -> Union[str, dict]:
        """Loads the session data from redis

        :return: The session data
        :rtype: Union[str, dict]
        """
        try:
            session_data = self.server.get(self.get_real_stored_key())
            return json.loads(force_str(session_data))
        except:
            return {}

    def custom_load(self, key: str) -> Union[dict, str]:
        """Loads a custom key from the session

        :param key: The key to load
        :type key: str
        :return: The value of the key
        :rtype: Union[dict, str]
        """
        try:
            session_data = self.server.get(key)
            return force_str(session_data)
        except:
            return {}

    def exists(self) -> bool:
        """Checks if the key exists in redis

        :return: True if exists, False otherwise
        :rtype: bool
        """
        return self.server.exists(self.get_real_stored_key())

    def create_or_update(self, session_data: Optional[dict] = dict()):
        """Creates or updates the session data on redis

        :param session_data: The session data
        :type session_data: Optional[dict]
        """
        if not self.django_session_id:
            raise InvalidSessionParameters("django_session_id is required for save/update")

        sessions = self.django_session_id

        if self.exists():
            data = self.load()
            sessions = f"{data.get('sessions', '')},{self.django_session_id}"
            session_data = session_data or data.get("payload")

            self.delete()

        body = {"sessions": sessions, "payload": session_data}
        self.save(body)

    def save(self, body: dict):
        """Saves the session data on redis

        :param body: The session data
        :type body: dict
        """
        logger.debug("Saving key: %s", self.keycloak_session_id)
        body = json.dumps(body)

        if redis.VERSION[0] >= 2:
            self.server.setex(
                self.get_real_stored_key(),
                self.get_expiry_age(),
                body
            )
        else:
            self.server.set(self.get_real_stored_key(), body)
            self.server.expire(self.get_real_stored_key(), self.get_expiry_age())

    def delete(self):
        """Deletes the session data from redis"""
        logger.debug("Deleting key: %s", self.keycloak_session_id)

        try:
            self.server.delete(self.get_real_stored_key())
        except:
            pass

    def get_real_stored_key(self) -> str:
        """Returns the key used to store the session data on redis

        :return: The key
        :rtype: str
        """
        return f"{self.REDIS_PREFIX}:{self.keycloak_session_id}"

    def get_expiry_age(self, **kwargs) -> int:
        """Returns the expiry age of the session data

        :return: The expiry age
        :rtype: int
        """
        return getattr(settings, "SESSION_REDIS_EXPIRATION", 3600 * 24 * 365)


class GenericSessionStorage:
    def __init__(self, key: str):
        self.server = RedisServer(None).get()
        self.key = key

    def load(self) -> Union[dict, str]:
        try:
            session_data = self.server.get(self.key)
            return force_str(session_data)
        except:
            return {}

    def delete(self):
        logger.debug("Deleting key: %s", self.key)

        try:
            self.server.delete(self.key)
        except:
            pass
