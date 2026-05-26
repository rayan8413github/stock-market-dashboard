import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector
import plotly.express as px

st.title("Stock Market Visualisation Dashboard")

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Rayan_sql8413",
    database = "stock_market"
)

query = """
SELECT * 
FROM stock_prices
"""

df = pd.read_sql(query, connection)
df["daily_return"] = df["close_price"].pct_change()*100

st.subheader("Stock Price data")
st.dataframe(df)

latest_close = df["close_price"].iloc[-1]
highest_price = df["high_price"].max()
lowest_price = df["low_price"].min()
average_close = df["close_price"].mean()

st.subheader("Stock Metrics")
col1, col2 = st.columns(2)

with col1:
    st.metric("Latest Close Price", round(latest_close, 2))
    st.metric("Highest Price", round(highest_price, 2))


with col2:
    st.metric("Lowest Price", round(lowest_price, 2))

    st.metric("Average Close Price", round(average_close, 2))


fig1 = px.line(
    df, x = "date", y = "close_price"
)

fig2 = px.line(
    df, x = "date", y = ["ma10", "close_price"]
)

col3 , col4 = st.columns(2)
with col3:
    st.subheader("Close price analysis")
    st.plotly_chart(fig1)

with col4:
    st.subheader("Close price vs moving average analysis")
    st.plotly_chart(fig2)

st.subheader("Trading Volume bar chart analysis")
# st.area_chart(df["volume"])
fig3 = px.area(
    df, x ="date", y = "volume"
)
st.plotly_chart(fig3)

col5, col6 = st.columns(2)
with col5:
   st.subheader("daily return area plot")
   fig4 = px.bar(
    df, x = "date", y = "daily_return", title= "daily return bar chart"
 )
   st.plotly_chart(fig4)

with col6:
   st.subheader("daily return histogram")
   fig5 = px.histogram(
    df,
    x="daily_return",
    nbins=30,
    title="Distribution of Daily Returns"
)
   st.plotly_chart(fig5)

# fig4 = px.histogram()

connection.close()