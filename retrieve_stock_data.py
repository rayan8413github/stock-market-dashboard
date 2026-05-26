import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "stock_market"
)

query = """
SELECT * FROM stock_prices
"""

df = pd.read_sql(query, connection)

# print(df.head(10))

plt.plot(df.index, df["close_price"])
plt.xlabel("id")
plt.ylabel("closing price")
plt.title("closing price analysis")
plt.show()
connection.close()