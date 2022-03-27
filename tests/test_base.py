import unittest
from unittest.mock import patch
from lendSaaS.client import LendClient
import pandas as pd

class BaseTestCase(unittest.TestCase):
    def setUpClass(self):
        self.lc = LendClient('api_key', 'client_name')

    @patch('lendSaaS.src.base_lend_saas.requests.get')
    def test_get_leads(self, mock_get):
        mock_get.return_value.status_code = 200
        response = self.lc.leads.get_leads(limit=1)
        self.assertEqual(response.status_code, 200)
        

if __name__ == '__main__':
    unittest.main()  