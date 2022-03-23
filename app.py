from src.base_lend_client import LendSaaSClient

def main():
    api_key = 'a8ea4f647e1cee2ef8823e9bdabce2e6'
    client = 'queen'
    ls = LendSaaSClient(api_key=api_key, client_name=client)
    # df = ls.leads.get_leads(limit=10)
    # lead = ls.leads.get_lead(76)
    # promise = ls.leads.get_lead_payment_promise(76)
    # external_data = ls.leads.get_lead_external_data(76, source='experian', product=['Credit Profile', 'Person Report'])
    notes = ls.leads.get_underwritting_info(submittedMinDate='2021-01-01', submittedMaxDate='2022-01-01')
    print(notes)
    # print(external_data)
    # print(lead)
    # print(promise)
    # print(df.head())

if __name__ == '__main__':
    main()