from lendSaaS.src.base_lend_saas import BaseLendSaas

class Funding(BaseLendSaas):

    def __init__(self, api_key, client_name):
        super().__init__(api_key, client_name=client_name)
        self.ENDPOINT_URL = '/lead'

    def get_account_monitoring(self, amStatusId, wlpId, includeClosedDeals='false'):
        """
        params: amStatusId=1 STR
        params: wipId=1 STR
        params: includeClosedDeals='true' BOOLEAN
        """
        body = {'amStatusId': amStatusId,
                'wlpId': wlpId,
                'includeClosedDeals': includeClosedDeals}

        return self.make_request('/snapshots/account-monitoring', 'POST', body=body)

    def get_funding_stats(self, sdate, edate):
        """
        params: sdate="2021-01-01" Datetime
        params: edate="2022-01-01" Datetime
        """
        body = {'sdate': sdate,
                'edate': edate,}

        return self.make_request('/snapshots/funding', 'POST', body=body)