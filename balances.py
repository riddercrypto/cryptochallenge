from binance.client import Client
import pandas as pd
import pprint

name = "Sir Twice as Nice"
publicapi = "IHx6h1oVKKTwODu6vYh7DvSPWZeiK42M6Rlin1UePAqMV4g9GWghpo2gvSLBRW2G"
secretapi = 'xJPr0P22RfRQ3LkxYoHiolhqPmXQDAadlt4GWdJUel3WLvHnPFajkon4Vrrjpo1P'

def get_balances(name,publicapi, secretapi):
    client = Client(publicapi,secretapi)
    account = client.get_account()
    balances = account.get('balances')
    df = pd.DataFrame(balances)
    df1= df.drop(df[(df['free'] == '0.00000000') & (df['locked'] == '0.00000000')].index)
    dfbalance=df1.rename(index=str, columns={"asset": "symbol"})
    dfbalance.free = dfbalance.free.astype(float)
    dfbalance.locked = dfbalance.locked.astype(float)
    dfbalance['amount'] = dfbalance['free'] + dfbalance['locked']
    del dfbalance['free']
    del dfbalance['locked']

    prices = client.get_all_tickers()
    prices2 = []
    for x in prices:
        if 'BTC' in x['symbol'][-3:]:
            x["symbol"]=x["symbol"][:-3]
            prices2.append(x)
    dfprices=pd.DataFrame(prices2)

    merged_df = dfbalance.merge(dfprices, how='left', on="symbol")
    merged_df[['price','amount']] = merged_df[['price','amount']].apply(pd.to_numeric)
    merged_df["total"]=merged_df['amount'] * merged_df['price']
    Totaal = merged_df['total'].sum()
    print(name)
    pprint.pprint(merged_df)
    print('Totaal in BTC = ' + str(Totaal))


get_balances(name,publicapi, secretapi)