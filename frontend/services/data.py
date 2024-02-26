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
from datetime import date, datetime

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
  
def DeleteStock(id):
  session.query(Stock).filter(Stock.id == id).delete()
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
      maturity_date=datetime.strptime(maturity_date, "%Y-%m-%d"),
      date_purchased=date.today()
      )

    session.add(instance)
    session.commit()
    return True

def DeleteBond(id):
  session.query(Bond).filter(Bond.id == id).delete()
  session.commit()
  return True

def AddProperty(id, property_type, property_name, value, location):
  portfolio = session.query(Portfolio).filter(Portfolio.user_id == id).one()
  if portfolio:
    instance = RealEstate(
      id=str(uuid.uuid4),
      property_name=property_name,
      property_type=property_type,
      value=value,
      location=location,
      portfolio_id=portfolio.id,
      date_purchased=date.today()
    )

    session.add(instance)
    session.commit()
    return True

def DeleteProperty(id):
  session.query(RealEstate).filter(RealEstate.id == id).delete()
  session.commit()
  return True

def AddOption(id, underlying_asset, contract_name, contract_type, expiration_date, price):
  portfolio = session.query(Portfolio).filter(Portfolio.user_id == id).one()
  if portfolio:
    instance = OptionsDerivatives(
      id=str(uuid.uuid4),
      contract_name=contract_name,
      underlying_asset=underlying_asset,
      contract_type=contract_type,
      portfolio_id=portfolio.id,
      expiration_date=datetime.strptime(expiration_date, "%Y-%m-%d"),
      price=price
    )

    session.add(instance)
    session.commit()
    return True

def DeleteOption(id):
  session.query(OptionsDerivatives).filter(OptionsDerivatives.id == id).delete()
  session.commit()
  return True

def AddPrivateEquity(id, commitment_amount, fund_name, investment_date, current_value):
  portfolio = session.query(Portfolio).filter(Portfolio.user_id == id).one()
  if portfolio:
    instance = PrivateEquity(
      id=str(uuid.uuid4),
      fund_name=fund_name,
      commitment_amount=commitment_amount,
      current_value=current_value,
      portfolio_id=portfolio.id,
      date_invested=datetime.strptime(investment_date, "%Y-%m-%d"),
    )

    session.add(instance)
    session.commit()
    return True
  
def DeletePrivateEquity(id):
  session.query(PrivateEquity).filter(PrivateEquity.id == id).delete()
  session.commit()
  return True

def AddCrypto(id, name, quantity, symbol, price):
  portfolio = session.query(Portfolio).filter(Portfolio.user_id == id).one()
  if portfolio:
    instance = Cryptocurrency(
      id=str(uuid.uuid4),
      name=name,
      symbol=symbol,
      quantity=quantity,
      portfolio_id=portfolio.id,
      price=price,
      date_purchased=date.today()
    )

    session.add(instance)
    session.commit()
    return True

def DeleteCrypto(id):
  session.query(Cryptocurrency).filter(Cryptocurrency.id == id).delete()
  session.commit()
  return True

def AddAccount(id, balance, account_name, account_type, currency):
  portfolio = session.query(Portfolio).filter(Portfolio.user_id == id).one()
  if portfolio:
    instance = CashAccount(
      id=str(uuid.uuid4),
      account_name=account_name,
      account_type=account_type,
      currency=currency,
      portfolio_id=portfolio.id,
      balance=balance,
    )

    session.add(instance)
    session.commit()
    return True
  
def DeleteAccount(id):
  session.query(CashAccount).filter(CashAccount.id == id).delete()
  session.commit()
  return True