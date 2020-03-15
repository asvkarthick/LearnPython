#!/usr/bin/python3
# Author: Karthick Kumaran <asvkarthick@gmail.com>
# Command to run: python3 internal_stock_analysis.py

import yfinance as yf
import pandas as pd
import datetime

today = datetime.datetime.now()
today_date = today.strftime("%Y-%m-%d")
print(today_date)

input_file = input("Enter Ticker file without .txt : ")
start_date = input("Enter start date (yyyy-mm-dd) : ")
end_date = input("Enter end date (yyyy-mm-dd) : ")

tickers = []
with open(input_file + '.txt', 'r') as f:
    for line in f:
        if line.strip():
            tickers.append(line.strip())

data = yf.download(tickers, start=start_date, end=end_date, group_by="ticker")
print(data)

close = []
diff = []
loss_percentage = []
start_close = []
end_close = []
for c in tickers:
    close.append(data[c]['Close'])
    i = len(data) - 1
    d = data[c]['Close'][i] - data[c]['Close'][0]
    diff.append(d)
    lp = ((data[c]['Close'][i] - data[c]['Close'][0]) / data[c]['Close'][0]) * 100
    loss_percentage.append(lp)
    start_close.append(data[c]['Close'][0])
    end_close.append(data[c]['Close'][i])

df = pd.concat(close, axis = 1, keys = tickers)
print(df)
df = df.T
df.to_csv('close_' + input_file + '_' + start_date + '_' + end_date + '.csv')

print("------------------------------------")
print("After Corona-Virus stocks difference")
df_diff = pd.DataFrame(diff, index = tickers, columns = ['Diff'])
print(df_diff)

print("------------------------------------")
print("Profit stocks")
profit_stocks = df_diff.loc[df_diff['Diff'] > 0.0]
print(profit_stocks)

print("------------------------------------")
print("Loss stocks")
loss_stocks = df_diff.loc[df_diff['Diff'] < 0.0]
print(loss_stocks)

print("------------------------------------")
print("Percentage difference")
df_loss_percentage = pd.DataFrame(loss_percentage, index = tickers, columns = ['Percentage'])
print(df_loss_percentage)

print("------------------------------------")
print("Percentage difference sorted")
df_loss_percentage.sort_values(by=['Percentage'], inplace = True)
print(df_loss_percentage)

df_lp = pd.DataFrame(loss_percentage, index = tickers, columns = ['Percentage'])
df_start = pd.DataFrame(start_close, index = tickers, columns = [start_date])
df_end = pd.DataFrame(end_close, index = tickers, columns = [end_date])
final_data = [df_lp, df_start, df_end, df_diff]
df_final_data = pd.concat(final_data, axis = 1)
print(df_final_data)
df_final_data.sort_values(by=['Percentage'], inplace = True)
print(df_final_data)
output_file = 'Stock_Analysis_Sorted_' + input_file + '_' + start_date + '_' + end_date + '.csv'
df_final_data.to_csv(output_file)
print(output_file)
output_file_unsorted = 'Stock_Analysis_' + input_file + '_' + start_date + '_' + end_date + '.csv'
data.to_csv(output_file_unsorted)
print(output_file_unsorted)
