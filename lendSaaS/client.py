from lendSaaS.src.leads import Leads
from lendSaaS.src.transactions import Transactions
from lendSaaS.src.underwriting import Underwriting
from lendSaaS.src.funding import Funding
from .__version__ import __version__


class LendClient:
    def __init__(self, api_key, client_name):
        self.leads = Leads(api_key, client_name)
        self.transactions = Transactions(api_key, client_name)
        self.underwriting = Underwriting(api_key, client_name)
        self.funding = Funding(api_key, client_name)

    def __str__(self):
        return f'LendClient {__version__}'

    def __repr__(self):
        return f'LendClient {__version__}'