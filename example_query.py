from numpy import product
from lendSaaS import LendClient
from dotenv import load_dotenv
load_dotenv()
import os

def main(): 
    api_key=os.getenv('api_key') 
    client=os.getenv('client')
    ls = LendClient(api_key=api_key, client_name=client)
    notes = ls.funding.get_funding_stats(sdate='2021-01-01', edate='2021-12-31')
                                            
    print(notes.iloc[0])


if __name__ == '__main__':
    main()