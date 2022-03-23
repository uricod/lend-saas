import unittest
from unittest.mock import patch
from lendSaaS.client import LendClient
import pandas as pd
import sys
sys.path.append('..')

class BaseTestCase(unittest.TestCase):
    @patch('LendSaaS.client.LendClient.leads.make_request')
    def test_get_leads(self, mock_make_request):
        mock_make_request.return_value = pd.DataFrame({'no data': ['no data returned']})
        self.lc.get_leads()
        mock_make_request.assert_called_with('/lead', 'GET')


if __name__ == '__main__':
    unittest.main()  