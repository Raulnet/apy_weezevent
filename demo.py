from api.weezevent_api import Api

# 1 find your access token
# -init api
api = Api('my_api_key')
response = api.post_auth_access_token('my_username', 'my_password')
# -set access_token && think to store it for next use
api.access_token = response.json()['accessToken']
# -api ready to use
events = api.get_events().json()
print(events)

# 2 with access_token stored
# -init api with token stored
api = Api('my_apy_key', 'my_access_token_stored')
# -api ready to use
events = api.get_events().json()
print(events)

# 3 request with parameters
parameters = {"include_not_published": True, "include_closed": True}
response = api.get_events(parameters)
print(response.json())

# 4 request with array parameters
parameters = {"id_event": [123456, 987654]}
response = api.get_participant_list(parameters)
print(response.json())
