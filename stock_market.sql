CREATE DATABASE stock_market;
USE stock_market;

CREATE TABLE stock_prices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    stock_symbol VARCHAR(20),
    date DATE,
    open_price FLOAT,
    high_price FLOAT,
    low_price FLOAT,
    close_price FLOAT,
    volume BIGINT,
    ma10 FLOAT
);
 
 
