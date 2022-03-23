import requests
from pandas import json_normalize

class BaseLendSaas:

    def __init__(self, api_key, client_name):
        self.BASE_URL = f'https://{client_name}.lendtech.io/backend/api/partners'

    def make_request(self, url, method, paramters=None):
        header = {'Content-type': 'application/json', 'X-API-KEY': self.api_key}
        if method == 'GET':
            result = requests.get(self.ENDPOINT_URL + url, headers=header, params=paramters)
        
        if result.status_code == 200:
            df =  json_normalize(result.json())
        
        return df

