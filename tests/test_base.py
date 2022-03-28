import unittest
from unittest.mock import patch
from lendSaaS.client import LendClient
import pandas as pd

class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.lc = LendClient('api_key', 'client_name')

    @patch('lendSaaS.src.base_lend_saas.requests.get')
    def test_get_leads(self, mock_get):
        mock_get.return_value = pd.DataFrame(data=[{'id': 1, 'name': 'test'}])
        response = self.lc.leads.get_leads(submittedMinDate='2022-01-01', 
                                           submittedMaxDate='2022-01-01', 
                                           offset=0, limit=10)
        self.assertEqual(type(response), pd.DataFrame)
        

if __name__ == '__main__':
    unittest.main()  