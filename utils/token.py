import http.client
import logging

import jwt
import environ
import json
from datetime import datetime, timedelta

env = environ.FileAwareEnv()

logger = logging.getLogger(__name__)

_token = None


class BearerToken(object):
    def __init__(self, j):
        data = json.loads(j)
        if 'access_token' in data:
            self.authorized = True
            self.access_token = data['access_token']
            self.expires_in = data['expires_in']
            self.expires_at = datetime.today() + timedelta(seconds=self.expires_in)
        else:
            self.authorized = False

    def should_refresh(self):
        # TODO - improve me
        # this is a naive approach to attempt refreshing the token before it expires
        # and leave some wiggle room to attempt retrying in case it fails (5 minutes)
        return self.expires_at <= (datetime.today() - timedelta(seconds=300))

    def is_valid(self):
        return self.authorized and (self.expires_at > datetime.today())


class IlsApiTokenRefresher(object):
    def __init__(self):
        self._token = get_bearer_token()

    def get_token(self):
        if self._token is None or not self._token.is_valid() or self._token.should_refresh():
            t = get_bearer_token()

            if self._token is None or t.is_valid():
                self._token = t

        return self._token


def get_bearer_token():
    """
    Gets a bearer token to access the ILS API.
    You should not always be getting a new token, only if the previous one expired / is about to expire.
    :return: BearerToken
    """
    client_id = env("ILS_EVENT_API_AUTH0_CLIENT_ID")
    client_secret = env("ILS_EVENT_API_AUTH0_CLIENT_SECRET")
    audience = env("ILS_EVENT_API_AUTH0_AUDIENCE")
    issuer = env("ILS_EVENT_API_AUTH0_ISSUER")

    conn = http.client.HTTPSConnection(issuer)
    payload = "{{\"client_id\":\"{client_id}\",\"client_secret\":\"{client_secret}\",\"audience\":\"{audience}\"," \
              "\"grant_type\":\"client_credentials\"}}" \
        .format(client_id=client_id, client_secret=client_secret, audience=audience)

    headers = {'content-type': "application/json"}

    conn.request("POST", "/oauth/token", payload, headers)

    res = conn.getresponse()
    data = res.read()

    response = data.decode("utf-8")
    token = BearerToken(response)

    if token.authorized:
        decoded = jwt.decode(token.access_token, client_secret, options={'verify_signature': False})
        logger.debug(f'ils api | authenticated with permissions: {decoded["permissions"]}')
    else:
        logger.error("ils api | not authorized!")

    return token
