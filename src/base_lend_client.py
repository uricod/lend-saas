from src.leads import Leads


class LendSaaSClient:
    def __init__(self, api_key, client_name):
        self.leads = Leads(api_key, client_name)