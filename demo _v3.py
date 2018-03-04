from api.weezevent_api_v3 import ApiV3

# #### API V3 ####
# Required account access ApiV3
# Required access_token find on class Api look ./demo.py
# -init ApiV3 like Api
api = ApiV3('my_apy_key', 'my_access_token_stored')

data = {
    "participants": [
        {
            "id_evenement": 123456,
            "id_billet": 987654,
            "email": "py.thon@weezevent.com",
            "nom": "Thon",
            "prenom": "Py",
        }
    ]
}

response = api.participants('POST', data)
print(response.json())
# @return
# {
#   'participants': [
#       {
#           'id_participant': '11223344',
#           'id_evenement': '123456',
#           'id_billet': 987654,
#           'email': 'pyt.thon@weezevent.com',
#           'nom': 'Thon',
#           'prenom': 'Py',
#           'idOrga': '987123',
#           'form': {
#               'prenom': 'Py',
#               'nom': 'Thon',
#               'email': 'py.thon@weezevent.com'
#           }
#       }
#   ],
#   'total_added': 1
# }
#
data = {
    "participants": [
        {
            'id_participant': '11223344',
            "id_evenement": 123456,
            "id_billet": 987654,
            "email": "pyt.hon@weezevent.com",
            "nom": "Hon",
            "prenom": "Pyt",
        }
    ]
}

response = api.participants('PATCH', data)
print(response.json())
# @return
# {
#   'participants': [
#       {
#           'id_participant': '11223344',
#           'id_evenement': '199367',
#           'id_billet': 1370106,
#           'email': 'pyt.thon@weezevent.com',
#           'nom': 'Hon',
#           'prenom': 'Pyt',
#           'idOrga': '987123',
#           'form': {
#               'prenom': 'Pyt',
#               'nom': 'Hon',
#               'email': 'pyt.thon@weezevent.com'
#           }
#       }
#   ],
#   'total_added': 1
# }
#
data = {
    "participants": [
        {
            'id_participant': '11223344',
            "id_evenement": 123456
        }
    ]
}
response = api.participants('DELETE', data)
print(response.json())
# @return
# {
#   'participants': [
#       {
#           'id_participant': '11223344',
#           'id_evenement': '123456',
#           'id_billet': 987654,
#           'email': 'pyt.thon@weezevent.com',
#           'nom': 'Hon',
#           'prenom': 'Pyt',
#           'only_if_not_used': False,
#           'allow_for_web': False,
#           'idOrga': '987123'
#       }
#   ],
#   'total_deleted': 1
#  }
#
