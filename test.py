from binance.client import Client
import pandas as pd
import pprint
import csv


class Balanceinfo:
    def parse(raw_file, delimiter):

        """Parses a raw csv file into a JSON line object"""
        # Open the CSV File
        opened_file = open(raw_file)
        # Read the CSV file
        csv_data =csv.reader(opened_file, delimiter=delimiter)
        # setup an empty list
        parsed_data = []
        # skip over the first line of the file for the headers
        fields = next(csv_data)
        # Build a data structure to return parsed data
        for row in csv_data:
            parsed_data.append(dict(zip(fields,row)))
        opened_file.close()
        return parsed_data

    # balance information
    def balance(apis):
        for x in apis:
            #Set Client and get token balances
            client = Client(x['publicapi'] ,x['secretapi'])
            account = client.get_account()
            balances = account.get('balances')
            df = pd.DataFrame(balances)
            dfcleanbalance = df.drop(df[(df['free'] == '0.00000000') & (df['locked'] == '0.00000000')].index)
            dfcleanbalance = dfcleanbalance.rename(index= str, columns= {"asset": "symbol"})

            #Get price per token
            prices = client.get_all_tickers()
            dfprices = pd.DataFrame(prices)
            dfcleanprices = dfprices[dfprices['symbol'].str[-3:]=="BTC"]
            dfcleanprices['symbol'] = dfcleanprices['symbol'].str[:-3]

            #merge prices per token with balances and get balance per token in BTC
            merged_df = dfcleanbalance.merge(dfcleanprices, how='left', on="symbol")
            merged_df[['free','locked','price']] = merged_df[['free','locked','price']].apply(pd.to_numeric)
            merged_df["total"]=(merged_df['free']+ merged_df['locked']) * merged_df['price']
            Totaal = merged_df['total'].sum()
            print(x['name'])
            pprint.pprint(merged_df)
            print('Totaal in BTC = ' + str(Totaal))
            print('')


apis = Balanceinfo.parse("/home/wouter/PycharmProjects/cryptochallenge/apis.csv", ",")

Balanceinfo.balance(apis)