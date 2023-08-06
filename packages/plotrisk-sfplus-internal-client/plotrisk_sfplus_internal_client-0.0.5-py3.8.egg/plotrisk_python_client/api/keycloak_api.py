import http.client

from plotrisk_python_client.util.auth_config import KeycloakConfig
from plotrisk_python_client.util.env_enums import EnvType


class KeycloakApi(object):

    @staticmethod
    def get_token(tenant, username, password, env, host=None):
        if host is not None:
            if env == EnvType.DEV:
                host = KeycloakConfig.DEV_AUTH
            if env == EnvType.QA:
                host = KeycloakConfig.QA_AUTH
            if env == EnvType.PROD:
                host = KeycloakConfig.PROD_AUTH
            if env == EnvType.PROD2:
                host = KeycloakConfig.PROD2_AUTH
        else:
            # default is PROD
            host = 'sso.sg.cropin.com'
        conn = http.client.HTTPSConnection(host)
        payload = 'client_id=web_app&username={}&password={}&grant_type=password'.format(username, password)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        conn.request("POST", "/auth/realms/{}/protocol/openid-connect/token".format(tenant), payload, headers)
        res = conn.getresponse()
        data = res.read()

        return data
