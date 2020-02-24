import yfinance as yf

msft = yf.Ticker("MSFT")
print("MSFT History")
print(msft.history(period="max"))
