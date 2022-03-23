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

    def get_stips(self, **kwargs):
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

        return self.make_request('/stips', 'GET', paramters=parameters)

    def get_principals(self, **kwargs):
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

        return self.make_request('/principals', 'GET', paramters=parameters)

    def get_banking_worksheet(self, **kwargs):
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

        return self.make_request('/banking-worksheet', 'GET', paramters=parameters)

    
    def get_uw_status_history(self, **kwargs):
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

        return self.make_request('/uw-status-history', 'GET', paramters=parameters)

    def get_lead_isos(self, **kwargs):
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

        return self.make_request('/lead-isos', 'GET', paramters=parameters)

    def get_syndication_info(self, **kwargs):
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

        return self.make_request('/syndication-info', 'GET', paramters=parameters)

    
    def get_fees(self, **kwargs):
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

        return self.make_request('/fees', 'GET', paramters=parameters)

    def get_external_data(self, **kwargs):
        """
        possible kwargs:
        params: leadId=int
        params: offset=0
        params: limit=100
        params: source:
                possible values:
                - experian
                - clear
                - datamerch
                - moneythumb
        params: product:
                possible values: (Comma Delimited list allowed)
                - Credit Profile
                - Premier Profile
                - Prequalification Credit Profile
                - Bank Statement
                - Person Report
                - Business Report
                - Datamerch
        """
        parameters = {}
        for arg in kwargs:
            if arg is not None:
                if arg is list:
                    parameters[arg] = ','.join(kwargs[arg])
                else:
                    parameters[arg] = kwargs[arg]

        return self.make_request('/external-data', 'GET', paramters=parameters)