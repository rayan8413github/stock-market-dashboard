import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

stock = yf.Ticker("AAPL")

data = stock.history(period = "6mo")
data["MA_10"] = data["Close"].rolling(window = 10).mean()

data.to_csv("Apple Stock Data.csv")

plt.plot(data.index, data["MA_10"], label = "10 days moving average")
plt.plot(data.index, data["Close"], label = "Close Price")

plt.title("Apple Share analysis")
plt.xlabel("dates")
plt.ylabel("price")

plt.legend()
plt.show()