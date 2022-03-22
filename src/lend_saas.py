import requests
from pandas import json_normalize

class LendSaas:

    def __init__(self) -> None:
        self.api_key = 'a8ea4f647e1cee2ef8823e9bdabce2e6'
        self.ENDPOINT_URL = 'https://queen.lendtech.io/backend/api/partners'

    def make_request(self, url, method):
        header = {'Content-type': 'application/json', 'X-API-KEY': self.api_key}
        if method == 'GET':
            result = requests.get(self.ENDPOINT_URL + url, headers=header)
        
        if result.status_code == 200:
            df =  json_normalize(result.json())
        
        return df

    def get_leads(self):
        url = '/leads'
        return self.make_request(url, 'GET')

