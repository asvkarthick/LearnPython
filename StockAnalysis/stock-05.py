import yfinance as yf
data = yf.download("AMZN AAPL", start="2020-01-01", end="2020-02-20", group_by="ticker")
print(data)
print(data['AMZN']['Close'])
