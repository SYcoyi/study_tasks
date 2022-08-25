# -*-coding:gbk -*-
import requests
import json as json_parser


class RestClient:
    def __init__(self, client_id, client_secret, api_root_url='http://localhost:8000'):
        self.token = None
        self.api_root_url = api_root_url
        self.session = requests.Session()
        self.login(client_id, client_secret)

    def login(self, client_id, client_secret):
        r = requests.post(self.api_root_url + "/oauth/2.0/token", data={"client_id": client_id,
                                                                        "client_secret": client_secret,
                                                                        "grant_type": "client_credentials"})
        token = r.json()['access_token']
        print(f"get the token = {token}")
        self.token = token

    def logout(self):
        self.token = None

