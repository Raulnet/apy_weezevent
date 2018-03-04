from api.core import CoreApi


class ApiV3(CoreApi):
    PARTICIPANTS = "/participants"

    def __init__(self, api_key, access_token=None):
        super().__init__(api_key, access_token)
        self.headers = {'content-type': 'application/x-www-form-urlencoded', 'charset': 'utf-8'}
        self.api_key = api_key
        self.access_token = access_token
        self.domain = "https://api.weezevent.com/v3"

    def participants(self, method, data):
        return self._request(method, self.PARTICIPANTS, {}, data)

    # TODO dev next route
