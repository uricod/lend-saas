import unittest
from unittest.mock import patch
import pandas as pd

class BaseTestCase(unittest.TestCase):
    @patch('lendSaaS.client.LendClient.leads.make_request')
    def test_get_leads(self, mock_make_request):
        mock_make_request.return_value = pd.DataFrame({'no data': ['no data returned']})
        self.lc.get_leads()
        mock_make_request.assert_called_with('/lead', 'GET')


     