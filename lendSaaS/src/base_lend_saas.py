import requests
from pandas import json_normalize
import pandas as pd

class BaseLendSaas:

    def __init__(self, api_key, client_name):
        self.api_key = api_key
        self.client_name = client_name
        self.BASE_URL = f'https://{self.client_name}.lendtech.io/backend/api/partners'

    def make_request(self, url, method, paramters=None, body=None):
        header = {'Content-type': 'application/json', 'X-API-KEY': self.api_key}
        if method == 'GET':
            result = requests.get(self.BASE_URL + url, headers=header, params=paramters)
        elif method == 'POST':
            result = requests.post(self.BASE_URL + url, headers=header, json=body)
        
        if result.status_code == 200:
            df =  json_normalize(result.json())
            if len(df) == 0:
                df = pd.DataFrame({'no data': ['no data returned']})
        
        elif result.status_code == 404:
            df = pd.DataFrame({'error': ['api url is not formed correctly - error 404']})

        elif result.status_code == 500:
            df = pd.DataFrame({'error': [result.json()['message']]})
        
        return df

