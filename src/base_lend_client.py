from src.leads import Leads
from src.transactions import Transactions


class LendSaaSClient:
    def __init__(self, api_key, client_name):
        self.leads = Leads(api_key, client_name)
        self.transactions = Transactions(api_key, client_name)