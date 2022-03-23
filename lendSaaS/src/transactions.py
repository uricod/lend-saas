from lendSaaS.src.base_lend_saas import BaseLendSaas

class Transactions(BaseLendSaas):

    def __init__(self, api_key, client_name):
        super().__init__(api_key, client_name=client_name)
        self.ENDPOINT_URL = '/transactions'

    def get_transactions(self, **kwargs):
        """
        possible kwargs:
        params: dateMin=2021-10-11
        params: dateMax=2021-10-11
        params: leadId=Int
        """
        parameters = {}
        for arg in kwargs:
            if arg is not None:
                parameters[arg] = kwargs[arg]

        return self.make_request(self.ENDPOINT_URL, 'GET', paramters=parameters)

    def get_transactions_details(self, **kwargs):
        """
        possible kwargs:
        params: datePostedMin=2021-10-11
        params: datePostedMax=2021-10-11
        params: dateUploadedMin=2021-10-11
        params: dateUploadedMax=2021-10-11
        params: leadId=Int
        """
        parameters = {}
        for arg in kwargs:
            if arg is not None:
                parameters[arg] = kwargs[arg]

        return self.make_request('/transactions-details', 'GET', paramters=parameters)
