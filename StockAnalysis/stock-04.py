import yfinance as yf

t = input("Enter Ticker: ")
ticker = yf.Ticker(t)
print(ticker)
print(t + " History")
print(ticker.history(period="max"))
