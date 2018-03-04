import requests
import json


class CoreApi:

    def __init__(self, api_key, access_token=None):
        self.domain = 'https://api.weezevent.com'
        self.headers = {'content-type': 'application/x-www-form-urlencoded', 'charset': 'utf-8'}
        self.api_key = api_key
        self.access_token = access_token

    def _request(self, method, action, params={}, data={}):
        if method == "GET":
            return self._request_get(action, params)
        if method == "POST":
            return self._request_post(action, params, data)
        if method == "PATCH":
            return self._request_patch(action, params, data)
        if method == "DELETE":
            return self._request_delete(action, params, data)

    def _request_get(self, action, params={}):
        params = self._get_params(params)
        url = self.domain + action
        return requests.get(url, params=params)

    def _request_post(self, action, params={}, data={}):
        url = self.domain + action
        params = self._get_params(params)
        data = {"data": json.dumps(data)}
        return requests.post(url, headers=self.headers, params=params, data=data)

    def _request_patch(self, action, params={}, data={}):
        url = self.domain + action
        params = self._get_params(params)
        data = {"data": json.dumps(data)}
        return requests.patch(url, headers=self.headers, params=params, data=data)

    def _request_delete(self, action, params={}, data={}):
        url = self.domain + action
        params = self._get_params(params)
        data = {"data": json.dumps(data)}
        return requests.delete(url, headers=self.headers, params=params, data=data)

    def _get_params(self, params={}):
        requests_params = Params(params)
        requests_params.api_key = self.api_key
        if self.access_token is not None:
            requests_params.access_token = self.access_token

        return requests_params.__dict__


class Params:
    ARRAY_PARAMETER = '[]'

    def __init__(self, params={}):
        self.api_key = None
        self.access_token = None
        for attr_key, attr_value in params.items():
            if isinstance(attr_value, list):
                attr_key += self.ARRAY_PARAMETER
            setattr(self, attr_key, attr_value)
