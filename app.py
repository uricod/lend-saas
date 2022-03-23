from base_lend_client import LendSaaSClient

def main():
    api_key = 'a8ea4f647e1cee2ef8823e9bdabce2e6'
    ls = LendSaaSClient(api_key=api_key)
    df = ls.leads.get_leads()

    print(df.head())

if __name__ == '__main__':
    main()