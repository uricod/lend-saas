from lendSaaS.src.base_lend_saas import BaseLendSaas

class Underwriting(BaseLendSaas):

    def __init__(self, api_key, client_name):
        super().__init__(api_key, client_name=client_name)

    def get_offers(self, **kwargs):
        """
        possible kwargs:
        params: leadId=int
        params: offset=0
        params: limit=1000
        """
        parameters = {}
        for arg in kwargs:
            if arg is not None:
                parameters[arg] = kwargs[arg]

        return self.make_request('/offers', 'GET', paramters=parameters)

    def get_positions(self, offset=0, limit=1000, **kwargs):
        """
        possible kwargs:
        params: offset=0 Required
        params: limit=1000 Required
        params: leadId=int
        """
        parameters = {}
        parameters['offset'] = offset
        parameters['limit'] = limit

        for arg in kwargs:
            if arg is not None:
                parameters[arg] = kwargs[arg]

        return self.make_request('/positions', 'GET', paramters=parameters)


    def get_offer(self, offer_id):
        '''
        params: offer_id = int
        '''
        return self.make_request(f'/offers/{offer_id}', 'GET')