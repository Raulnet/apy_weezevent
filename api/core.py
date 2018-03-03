import requests


class CoreApi:
    AUTH_ACCESS_TOKEN = '/auth/access_token'

    def __init__(self, api_key, access_token=None):
        self.domain = 'https://api.weezevent.com'
        self.api_key = api_key
        self.access_token = access_token

    def _request_get(self, action, params={}):
        params = self._get_params(params)
        url = self.domain + action
        return requests.get(url, params=params)

    def _request_post(self, action, params={}, data=None):
        url = self.domain + action
        headers = {'content-type': 'application/x-www-form-urlencoded', 'charset': 'utf-8'}

        return requests.post(url, headers=headers, params=params, data=data)

    def _get_params(self, params={}):
        requests_params = Params(params)
        requests_params.api_key = self.api_key
        if self.access_token is None:
            raise Exception("access token undefined")

        requests_params.access_token = self.access_token
        return requests_params.__dict__

    def post_auth_access_token(self, username, password):
        params = Params({"username": username, "password": password})
        params.api_key = self.api_key

        return self._request_post(self.AUTH_ACCESS_TOKEN, params.__dict__)


class Params:
    ARRAY_PARAMETER = '[]'

    def __init__(self, params={}):
        self.api_key = None
        self.access_token = None
        for attr_key, attr_value in params.items():
            if isinstance(attr_value, list):
                attr_key += self.ARRAY_PARAMETER
            setattr(self, attr_key, attr_value)
