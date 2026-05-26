import yfinance as yf
import pandas as pd
import mysql.connector

stock = yf.Ticker("AAPL")
data = stock.history(period = "3mo")

data["MA10"] = data["Close"].rolling(window = 10).mean()
data.reset_index(inplace = True)

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "stock_market"
)

cursor = connection.cursor()

query = """INSERT INTO stock_prices
(stock_symbol, date, open_price, high_price,
low_price, close_price, volume, ma10)

VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""


for index, row in data.iterrows():
    values = (
        "AAPL",
        row["Date"].date(),
        float(row["Open"]),float(row["High"]),float(row["Low"]),
        float(row["Close"]), int(row["Volume"]),
        None if pd.isna(row["MA10"]) else float(row["MA10"])
    )

    cursor.execute(query, values)

connection.commit()

print("Data saved succesfully.")

cursor.close()
connection.close()