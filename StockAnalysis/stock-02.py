import matplotlib.pyplot as plt
import yfinance as yf  
 
# Get the data of the stock AMZN
data = yf.download('AMZN','2020-01-01','2020-02-20')
 
# Plot the close price of the AMZN
data.Close.plot()
plt.show()
