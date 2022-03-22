from src.lend_saas import LendSaas

def main():
    lend_saas = LendSaas()
    df = lend_saas.get_leads()

    print(df.head())
    df.to_csv('leads.csv', index=False)

if __name__ == '__main__':
    main()