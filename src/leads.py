from src.base_lend_saas import BaseLendSaas

class Leads(BaseLendSaas):

    def __init__(self, api_key, client_name):
        super().__init__(api_key, client_name=client_name)
        self.ENDPOINT_URL = '/leads'

    def get_leads(self, **kwargs):
        """
        possible kwargs:
        submittedMinDate=2021-10-11
        submittedMaxDate=2021-10-11
        offset=0
        limit=1000
        """
        parameters = {}
        for arg in kwargs:
            if arg is not None:
                parameters[arg] = kwargs[arg]

        return self.make_request(self.ENDPOINT_URL, 'GET', paramters=parameters)