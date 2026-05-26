# Stock Market Visualization Dashboard

A beginner-to-intermediate data analytics dashboard project built using Python, MySQL, Streamlit, and Plotly for analyzing real stock market data.

---

## Project Overview

This project fetches real-time stock market data using Yahoo Finance, stores it in a MySQL database, and visualizes the data through an interactive Streamlit dashboard.

The dashboard provides:
- stock price trends
- moving average analysis
- trading volume analysis
- daily returns analysis
- return distribution visualization

---

## Features

- Fetch stock data using `yfinance`
- Store stock data in MySQL
- Retrieve and process data using Pandas
- Interactive dashboard using Streamlit
- Data visualization using Plotly
- Moving Average (MA10) calculation
- Daily Return calculation
- Histogram analysis for return distribution

---

## Tech Stack

- Python
- Pandas
- MySQL
- Streamlit
- Plotly
- yfinance

---

## Dashboard Visualizations

### 1. Closing Price Trend
Shows the overall stock movement over time.

### 2. Moving Average Analysis
Compares closing price with 10-day moving average.

### 3. Trading Volume Analysis
Displays daily trading activity.

### 4. Daily Returns Analysis
Shows percentage change in stock price day-by-day.

### 5. Daily Return Distribution Histogram
Analyzes frequency distribution of stock returns.

---

## Project Structure

```text
stock-market-dashboard/
│
├── app.py
├── retrieve_stock_data.py
├── store_stock_data.py
├── stock_fetch.py
├── stock_market.sql
├── requirements.txt
├── .gitignore
└── README.md
