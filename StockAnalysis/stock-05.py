import yfinance as yf
import pandas as pd

data = yf.download("AMZN AAPL", start="2020-02-20", end="2020-02-26", group_by="ticker")
close_amzn = data['AMZN']['Close']
close_aapl = data['AAPL']['Close']

close = [close_amzn, close_aapl]
df = pd.concat(close, axis = 1, keys = ['AMZN', 'AAPL'])
print(df)
