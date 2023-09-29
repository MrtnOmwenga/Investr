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
from models.engine import session

import uuid
from datetime import date

def AddStock(id, symbol, name, quantity, price):
  portfolio = session.query(Portfolio).filter(Portfolio.user_id == id).one()
  if portfolio:
    instance = Stock(
      id=str(uuid.uuid4()),
      portfolio_id=portfolio.id,
      symbol=symbol,
      company_name=name,
      quantity=quantity,
      price=price,
      date_purchased=date.today()
      )

    session.add(instance)
    session.commit()
    return True
  
def AddBond(id, issuer, face_value, yield_rate, maturity_date):
  portfolio = session.query(Portfolio).filter(Portfolio.user_id == id).one()
  if portfolio:
    instance = Bond(
      id=str(uuid.uuid4()),
      portfolio_id=portfolio.id,
      issuer=issuer,
      face_value=face_value,
      yield_rate=yield_rate,
      maturity_date=maturity_date,
      date_purchased=date.today()
      )

    session.add(instance)
    session.commit()
    return True