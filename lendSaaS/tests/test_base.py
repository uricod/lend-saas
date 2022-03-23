import unittest
from unittest.mock import patch
from lendSaaS.client import LendClient
import pandas as pd

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.lc = LendClient('api_key', 'client_name')

    @patch('LendClient.make_request')
    def test_get_leads(self, mock_make_request):
        mock_make_request.return_value = pd.DataFrame({'no data': ['no data returned']})
        self.lc.get_leads()
        mock_make_request.assert_called_with('/lead', 'GET')

    def tearDown(self):
        pass
     