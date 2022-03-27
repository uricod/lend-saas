from numpy import product
from lendSaaS import LendClient
from dotenv import load_dotenv
load_dotenv()
import os

def main(): 
    api_key=os.getenv('api_key') 
    client=os.getenv('client')
    lc = LendClient(api_key=api_key, client_name=client)
    notes = lc.leads.get_leads(limit=1)
                                            
    print(notes.iloc[0])


if __name__ == '__main__':
    main()