import sys
sys.path.append('C:/Users/Admin/Documents/Portfolio/investr/backend/assets')

from sqlalchemy.orm import sessionmaker

from models import Base
from models.crypto_data import CryptocurrencyData
from models.etf_data import ETFData
from models.stock_data import StockData
from models.fund_data import FundData

from models.engine import engine

print('CREATING TABLES')
Base.metadata.create_all(bind=engine)