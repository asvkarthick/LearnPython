import yfinance as yf
import pandas as pd

tickers = []
with open("stocks.txt", 'r') as f:
    for line in f:
        #tickers.append(f'"{line.strip}"')
        tickers.append(line.strip())

data = yf.download(tickers, start="2020-02-20", end="2020-02-26", group_by="ticker")

close = []
diff = []
for c in tickers:
    close.append(data[c]['Close'])
    d = 0
    i = 1
    while i < len(data):
        d = d + data[c]['Close'][i] - data[c]['Close'][i - 1]
        i = i + 1
    diff.append(d)

df = pd.concat(close, axis = 1, keys = tickers)
print(df)

print()
print("After Corona-Virus stocks difference")
df_diff = pd.DataFrame(diff, index = tickers)
print(df_diff)
