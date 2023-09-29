import sys
sys.path.append('C:/Users/Admin/Documents/Portfolio/investr')

from sqlalchemy.orm import sessionmaker

from models import Base
from models.users import Users
from models.portfolio import Portfolio
from models.bonds import Bond
from models.cash import CashAccount
from models.crypto import Cryptocurrency
from models.eft import ETF
from models.fund import Fund
from models.options import OptionsDerivatives
from models.private_equity import PrivateEquity
from models.real_estate import RealEstate
from models.reit import REIT
from models.stocks import Stock

from models.engine import engine

print('CREATING TABLES')
Base.metadata.create_all(bind=engine)
