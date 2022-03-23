from lendSaaS.client import LendClient
from dotenv import load_dotenv
load_dotenv()
import os

def main(): 
    api_key=os.getenv('api_key') 
    client=os.getenv('client')
    ls = LendClient(api_key=api_key, client_name=client)
    notes = ls.transactions.get_transactions_details(datePostedMin='2021-01-01', datePostedMax='2022-01-01')
    print(notes.iloc[0])


if __name__ == '__main__':
    main()