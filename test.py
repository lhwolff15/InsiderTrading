import InsiderTrading as IT
from datetime import date, timedelta
import yfinance as yf
stock_name = "MSFT"

stock = yf.Ticker(stock_name)
print(float(stock.info["previousClose"]))
print(str(date.today()-timedelta(1)))

print(IT.insider_trading())