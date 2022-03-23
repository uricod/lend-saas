from src.base_lend_saas import BaseLendSaas

class Leads(BaseLendSaas):

    def __init__(self, api_key, client_name):
        super().__init__(api_key, client_name=client_name)
        self.ENDPOINT_URL = '/lead'

    def get_leads(self, **kwargs):
        """
        possible kwargs:
        params: submittedMinDate=2021-10-11
        params: submittedMaxDate=2021-10-11
        params: offset=0
        params: limit=1000
        """
        parameters = {}
        for arg in kwargs:
            if arg is not None:
                parameters[arg] = kwargs[arg]

        return self.make_request(self.ENDPOINT_URL + 's', 'GET', paramters=parameters)

    def get_lead(self, lead_id):
        '''
        params: lead_id = int
        '''
        return self.make_request(f'{self.ENDPOINT_URL}/{lead_id}', 'GET')

    def get_lead_payment_promise(self, lead_id):
        return self.make_request(f'{self.ENDPOINT_URL}/{lead_id}/payment-promise', 'GET')

    def get_lead_external_data(self, lead_id, **kwargs):
        """
        possible kwargs:
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

        return self.make_request(f'{self.ENDPOINT_URL}/{lead_id}', 'GET', paramters=parameters)

    def get_notes(self, **kwargs):
        """
        possible kwargs:
        One of These arguments must be passed:
        params: leadId = int
        params: startDate = 2021-10-11
        params: endDate = 2021-10-11
        params: offset = 0
        params: limit = 5000
        """
        parameters = {}
        for arg in kwargs:
            if arg is not None:
                parameters[arg] = kwargs[arg]

        return self.make_request('/notes', 'GET', paramters=parameters)

    def get_ach_schedule(self, **kwargs):
        """
        possible kwargs:
        One of These arguments must be passed:
        params: leadId = int
        params: startDate = 2021-10-11
        params: endDate = 2021-10-11
        params: offset = 0
        params: limit = 5000
        """
        parameters = {}
        for arg in kwargs:
            if arg is not None:
                parameters[arg] = kwargs[arg]

        return self.make_request('/ach-schedule', 'GET', paramters=parameters)

    def get_underwritting_info(self, **kwargs):
        """
        possible kwargs:
        One of These arguments must be passed:
        params: leadId = int
        params: submittedMinDate=2021-10-11
        params: submittedMaxDate=2021-10-11
        params: offset = 0
        params: limit = 5000
        """
        parameters = {}
        for arg in kwargs:
            if arg is not None:
                parameters[arg] = kwargs[arg]

        return self.make_request('/underwriting-info', 'GET', paramters=parameters)


    