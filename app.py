from lendSaaS.client import LendClient

def main():
    api_key = 'a8ea4f647e1cee2ef8823e9bdabce2e6'
    client = 'queen'
    ls = LendClient(api_key=api_key, client_name=client)
    notes = ls.transactions.get_transactions_details(datePostedMin='2021-01-01', datePostedMax='2022-01-01')
    print(notes.iloc[0])


if __name__ == '__main__':
    main()