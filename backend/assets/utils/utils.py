from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from models.engine import session as AssetSession
from users.models.engine import session as UserSession
from users.models.users import Users
from users.models.portfolio import Portfolio
from users.models.bonds import Bond
from users.models.cash import CashAccount
from users.models.crypto import Cryptocurrency
from users.models.eft import ETF
from users.models.fund import Fund
from users.models.options import OptionsDerivatives
from users.models.private_equity import PrivateEquity
from users.models.real_estate import RealEstate
from users.models.reit import REIT
from users.models.stocks import Stock

def get_unique_symbols():

  try:
    # Query unique symbols from each table
    stock_symbols = UserSession.query(Stock.symbol).distinct().all()
    crypto_symbols = UserSession.query(Cryptocurrency.symbol).distinct().all()
    etf_symbols = UserSession.query(ETF.symbol).distinct().all()
    fund_symbols = UserSession.query(Fund.symbol).distinct().all()

    # Combine all symbols into a single list
    all_symbols = [symbol[0] for symbol in stock_symbols]
    all_symbols.extend(symbol[0] for symbol in crypto_symbols)
    all_symbols.extend(symbol[0] for symbol in etf_symbols)
    all_symbols.extend(symbol[0] for symbol in fund_symbols)

    # Get unique symbols by converting the list to a set
    unique_symbols = set(all_symbols)

    return unique_symbols, { "stocks": [symbol[0] for symbol in stock_symbols], "crypto": [symbol[0] for symbol in crypto_symbols], "etfs": [symbol[0] for symbol in etf_symbols], "funds": [symbol[0] for symbol in fund_symbols] }

  except InvalidRequestError as e:
    print("Invalid request:", e)
    return None

  finally:
    # Close the session
    UserSession.close()

def calculate_average_price(data):
  total_price = 0
  count = 0
  for entry in data:
    if isinstance(entry, dict) and 'close' in entry:
      total_price += entry['close']
      count += 1
  if count == 0:
    return 0  # Return 0 if no valid entries found
  average_price = total_price / count
  return average_price

def update_average_price(session, Model, symbol, average_price):
  asset = AssetSession.query(Model).filter_by(symbol=symbol).first()
  if asset:
    asset.price = average_price
  else:
    asset = Model(symbol=symbol, price=average_price, date=datetime.now())
    session.add(asset)
  AssetSession.commit()

def chunk_list(lst=[], chunk_size=100):
  """Split a list into chunks of the specified size."""
  lst = list(lst)
  for i in range(0, len(lst), chunk_size):
      yield lst[i:i + chunk_size]
