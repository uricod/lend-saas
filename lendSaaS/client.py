from lendSaaS.src.leads import Leads
from lendSaaS.src.transactions import Transactions


class LendClient:
    def __init__(self, api_key, client_name):
        self.leads = Leads(api_key, client_name)
        self.transactions = Transactions(api_key, client_name)