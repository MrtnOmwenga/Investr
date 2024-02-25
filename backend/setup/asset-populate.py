import sys
import requests
from datetime import datetime, timedelta

sys.path.append('C:/Users/Admin/Documents/Portfolio/investr')

from config import API_KEY

from asset_models import Base
from asset_models.crypto_data import CryptocurrencyData
from asset_models.stock_data import StockData
from asset_models.etf_data import ETFData


# List of symbols
symbols = ["AAPL", "GOOGL", "MSFT", "AMZN"]

# Get yesterday's date
yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

# Alpha Vantage API endpoint for time series (daily) for multiple symbols
symbol_str = ",".join(symbols)
endpoint = f"https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols={symbol_str}&apikey={API_KEY}"

try:
    # Make the API request
    response = requests.get(endpoint)
    data = response.json()

    # Extract yesterday's closing prices for each symbol
    for quote in data["Stock Quotes"]:
        symbol = quote["1. symbol"]
        closing_price_yesterday = quote["2. price"]
        print(f"Yesterday's closing price for {symbol}: {closing_price_yesterday}")
except Exception as e:
    print(f"Error fetching data: {e}")
