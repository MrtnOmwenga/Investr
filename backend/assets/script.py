from utils.marketstack_api import fetch_bulk_eod_data
from models.engine import session
from models.stock_data import StockData
from models.fund_data import FundData
from models.etf_data import ETFData
from models.crypto_data import CryptocurrencyData
from utils.utils import get_unique_symbols, chunk_list, calculate_average_price, update_average_price

# Adjust the batch size according to your API rate limit
BATCH_SIZE = 100

def fetch_and_update_assets_data():
  symbols, data = get_unique_symbols()
  symbol_batches = chunk_list(symbols, BATCH_SIZE)

  for batch in symbol_batches:
    eod_data = fetch_bulk_eod_data(batch)
    for symbol_data in eod_data:
      if not symbol_data:  # Skip empty entries
        continue
      average_price = calculate_average_price(symbol_data)
      symbol = symbol_data['symbol']
      print(data)
      if symbol in data['crypto']:
        update_average_price(session, CryptocurrencyData, symbol, average_price)
      elif symbol in data['etfs']:
        update_average_price(session, ETFData, symbol, average_price)
      elif symbol in data['funds']:
        update_average_price(session, Fund, symbol, average_price)
      elif symbol in data['stocks']:
        update_average_price(session, StockData, symbol, average_price)

if __name__ == "__main__":
  fetch_and_update_assets_data()
