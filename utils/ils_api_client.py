from __future__ import print_function

import environ

import core.ils.client
from utils.token import IlsApiTokenRefresher

env = environ.FileAwareEnv()


def get_client(token_refresher: IlsApiTokenRefresher) -> core.ils.client.ApiClient:
    configuration = core.ils.client.Configuration()

    token = token_refresher.get_token()
    configuration.access_token = token.access_token

    # uncomment if you want to debug calls
    # configuration.debug = True

    configuration.host = f'{env("ILS_EVENT_API_AUTH0_AUDIENCE")}'

    return core.ils.client.ApiClient(configuration)
