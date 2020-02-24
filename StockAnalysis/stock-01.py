import matplotlib.pyplot as plt
import yfinance as yf  
 
# Get the data of the stock AAPL
data = yf.download('AAPL','2020-01-01','2020-02-20')
 
# Plot the close price of the AAPL
data.Close.plot()
plt.show()
