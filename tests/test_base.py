import unittest
from unittest.mock import patch
import pandas as pd

class BaseTestCase(unittest.TestCase):
    @patch('lendSaaS.src.base_lend_saas.requests.get')
    def test_get_leads(self, mock_make_request):
        mock_make_request.return_value = pd.DataFrame({'no data': ['no data returned']})
        mock_make_request.assert_called_with('/lead', 'GET')

if __name__ == '__main__':
    unittest.main()  