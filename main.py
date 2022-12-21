from api import apikey, secret
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd

def main_func():
    client = Client(apikey, secret)
    tickers = client.get_all_tickers()
    ticker_df = pd.DataFrame(tickers)
    print(ticker_df.loc['symbol':'XRPBUSD', 'price'])
    for item in tickers:
        if item['symbol'] == 'XRPBUSD':
            print(f"{item['symbol']}:{item['price']}")

if __name__ == '__main__':
    main_func()



