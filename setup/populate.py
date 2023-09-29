import uuid
import bcrypt
from datetime import datetime

import sys
sys.path.append('C:/Users/Admin/Documents/Portfolio/investr')

from models import Base
from models.users import Users #
from models.portfolio import Portfolio #
from models.bonds import Bond #
from models.cash import CashAccount #
from models.crypto import Cryptocurrency #
from models.eft import ETF #
from models.fund import Fund #
from models.options import OptionsDerivatives #
from models.private_equity import PrivateEquity #
from models.real_estate import RealEstate #
from models.reit import REIT #
from models.stocks import Stock #

from models.engine import session


password = 'foobar'
bytes = password.encode('utf-8')

date_format = "%Y-%m-%d"

UsersList = [
  {
    "id": str(uuid.uuid4()),
    "name": "Rajesh Koothrapali",
    "email": "rajeshkoothrapali@gmail.com",
    "password": bcrypt.hashpw(bytes, bcrypt.gensalt()).decode('utf-8')
  },
  {
    "id": str(uuid.uuid4()),
    "name": "Sheldon Cooper",
    "email": "sheldoncooper@gmail.com",
    "password": bcrypt.hashpw(bytes, bcrypt.gensalt()).decode('utf-8')
  },
  {
    "id": str(uuid.uuid4()),
    "name": "Leonard Hofstadter",
    "email": "leonardhofstadter@gmail.com",
    "password": bcrypt.hashpw(bytes, bcrypt.gensalt()).decode('utf-8')
  }
]


for user in UsersList:
  instance = Users(id=user["id"], name=user["name"], email=user["email"], password=user["password"])
  session.add(instance)


PortfolioList = [
  {
    "name": 'Portfolio 1',
    "user_id": UsersList[0]["id"],
    "id": str(uuid.uuid4())
  },
  {
    "name": 'Portfolio 2',
    "user_id": UsersList[1]["id"],
    "id": str(uuid.uuid4())
  },
  {
    "name": 'Portfolio 3',
    "user_id": UsersList[2]["id"],
    "id": str(uuid.uuid4())
  }
]

for portfolio in PortfolioList:
  instance = Portfolio(id=portfolio["id"], user_id=portfolio["user_id"], name=portfolio["name"])
  session.add(instance)


StockList = [
  {
    "id": str(uuid.uuid4()),
    "symbol": 'AAPL',
    "company_name": 'Apple Inc.',
    "quantity": 200,
    "price": 150.0,
    "date_purchased": datetime.strptime('2023-01-15', date_format),
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "symbol": 'AAPL',
    "company_name": 'Apple Inc.',
    "quantity": 200,
    "price": 150.0,
    "date_purchased": datetime.strptime('2023-01-15', date_format),
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "symbol": 'AAPL',
    "company_name": 'Apple Inc.',
    "quantity": 200,
    "price": 150.0,
    "date_purchased": datetime.strptime('2023-01-15', date_format),
    "portfolio_id": PortfolioList[2]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "symbol": 'GOOGL',
    "company_name": 'Alphabet Inc.',
    "quantity": 200,
    "price": 2700.0,
    "date_purchased": datetime.strptime('2023-02-20', date_format),
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "symbol": 'GOOGL',
    "company_name": 'Alphabet Inc.',
    "quantity": 200,
    "price": 2700.0,
    "date_purchased": datetime.strptime('2023-02-20', date_format),
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "symbol": 'GOOGL',
    "company_name": 'Alphabet Inc.',
    "quantity": 200,
    "price": 2700.0,
    "date_purchased": datetime.strptime('2023-02-20', date_format),
    "portfolio_id": PortfolioList[2]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "symbol": 'MSFT',
    "company_name": 'Microsoft Corporation',
    "quantity": 200,
    "price": 290.0,
    "date_purchased": datetime.strptime('2023-03-10', date_format),
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "symbol": 'MSFT',
    "company_name": 'Microsoft Corporation',
    "quantity": 200,
    "price": 290.0,
    "date_purchased": datetime.strptime('2023-03-10', date_format),
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "symbol": 'MSFT',
    "company_name": 'Microsoft Corporation',
    "quantity": 200,
    "price": 290.0,
    "date_purchased": datetime.strptime('2023-03-10', date_format),
    "portfolio_id": PortfolioList[2]["id"]
  }
]

for stock in StockList:
  instance = Stock(
    id=stock["id"],
    symbol=stock["symbol"],
    company_name=stock["company_name"],
    quantity=stock["quantity"],
    price=stock["price"],
    date_purchased=stock["date_purchased"],
    portfolio_id=stock["portfolio_id"]
    )
  session.add(instance)

FundList = [
 {
  "id": str(uuid.uuid4()),
  "fund_name": 'Sample Mutual Fund',
  "symbol": 'MUTFUND1',
  "nav": 150.0,
  "date_purchased": datetime.strptime('2023-01-15', date_format),
  "portfolio_id": PortfolioList[0]["id"],
  "fund_type": 'Mutual Fund'
 },
 {
  "id": str(uuid.uuid4()),
  "fund_name": 'Sample Index Fund',
  "symbol": 'INDEXFUND1',
  "nav": 2700.0,
  "date_purchased": datetime.strptime('2023-02-20', date_format),
  "portfolio_id": PortfolioList[1]["id"],
  "fund_type": 'Index Fund'
 },
 {
  "id": str(uuid.uuid4()),
  "fund_name": 'Sample Hedge Fund',
  "symbol": 'HEDGEFUND1',
  "nav": 290.0,
  "date_purchased": datetime.strptime('2023-03-10', date_format),
  "portfolio_id": PortfolioList[2]["id"],
  "fund_type": 'Hedge Fund'
 }
]

for fund in FundList:
  instance = Fund(
    id=fund["id"],
    fund_name=fund["fund_name"],
    symbol = fund["symbol"],
    nav = fund["nav"],
    date_purchased=fund["date_purchased"],
    portfolio_id=fund["portfolio_id"],
    fund_type = fund["fund_type"]
    )
  session.add(instance)

ReitList = [
  {
    "id": str(uuid.uuid4()),
    "property_name": 'Sample REIT 1',
    "symbol": 'REIT1',
    "price_per_share": 75.0,
    "date_purchased": datetime.strptime('2023-01-15', date_format),
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "property_name": 'Sample REIT 2',
    "symbol": 'REIT2',
    "price_per_share": 90.0,
    "date_purchased": datetime.strptime('2023-02-20', date_format),
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "property_name": 'Sample REIT 3',
    "symbol": 'REIT3',
    "price_per_share": 80.0,
    "date_purchased": datetime.strptime('2023-03-10', date_format),
    "portfolio_id": PortfolioList[2]["id"]
  }
]

for reit in ReitList:
  instance = REIT(
    id = reit["id"],
    property_name=reit["property_name"],
    symbol=reit["symbol"],
    price_per_share=reit["price_per_share"],
    date_purchased=reit["date_purchased"],
    portfolio_id=reit["portfolio_id"]
    )
  session.add(instance)

OptionsList = [
  {
    "id": str(uuid.uuid4()),
    "contract_name": 'Sample Option 1',
    "underlying_asset": 'AAPL',
    "contract_type": 'Call',
    "expiration_date": datetime.strptime('2023-05-15', date_format),
    "price": 10.0,
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "contract_name": 'Sample Option 2',
    "underlying_asset": 'GOOGL',
    "contract_type": 'Put',
    "expiration_date": datetime.strptime('2023-06-20', date_format),
    "price": 12.0,
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "contract_name": 'Sample Option 3',
    "underlying_asset": 'MSFT',
    "contract_type": 'Call',
    "expiration_date": datetime.strptime('2023-07-10', date_format),
    "price": 8.0,
    "portfolio_id": PortfolioList[2]["id"]
  }
]

for option in OptionsList:
  instance = OptionsDerivatives(
    id=option["id"],
    contract_name=option["contract_name"],
    contract_type=option["contract_type"],
    underlying_asset=option["underlying_asset"],
    expiration_date=option["expiration_date"],
    price=option["price"],
    portfolio_id=option["portfolio_id"]
    )
  session.add(instance)

CryptoList = [
  {
    "id": str(uuid.uuid4()),
    "name": 'Bitcoin',
    "symbol": 'BTC',
    "price": 45000.0,
    "date_purchased": datetime.strptime('2023-01-15', date_format),
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "name": 'Ethereum',
    "symbol": 'ETH',
    "price": 3000.0,
    "date_purchased": datetime.strptime('2023-02-20', date_format),
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "name": 'Litecoin',
    "symbol": 'LTC',
    "price": 150.0,
    "date_purchased": datetime.strptime('2023-03-10', date_format),
    "portfolio_id": PortfolioList[2]["id"]
  }
]

for crypto in CryptoList:
  instance = Cryptocurrency(
    id=crypto["id"],
    name=crypto["name"],
    symbol=crypto["symbol"],
    price=crypto["price"],
    date_purchased=crypto["date_purchased"],
    portfolio_id=crypto["portfolio_id"]
    )
  session.add(instance)

EquityList = [
  {
    "id": str(uuid.uuid4()),
    "fund_name": 'Private Equity Fund 1',
    "date_invested": datetime.strptime('2023-01-15', date_format),
    "commitment_amount": 50000.0,
    "current_value": 55000.0,
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "fund_name": 'Private Equity Fund 2',
    "date_invested": datetime.strptime('2023-02-20', date_format),
    "commitment_amount": 75000.0,
    "current_value": 80000.0,
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "fund_name": 'Private Equity Fund 3',
    "date_invested": datetime.strptime('2023-03-10', date_format),
    "commitment_amount": 60000.0,
    "current_value": 63000.0,
    "portfolio_id": PortfolioList[2]["id"]
  }
]

for equity in EquityList:
  instance = PrivateEquity(
    id=equity["id"],
    fund_name=equity["fund_name"],
    date_invested=equity["date_invested"],
    commitment_amount=equity["commitment_amount"],
    current_value=equity["current_value"],
    portfolio_id=equity["portfolio_id"]
  )
  session.add(instance)


BondList = [
  {
    "id": str(uuid.uuid4()),
    "issuer": "Government of XYZ",
    "face_value": 1000.0,
    "yield_rate": 3.5,
    "maturity_date": datetime.strptime('2025-12-31', date_format),
    "date_purchased": datetime.strptime('2023-01-15', date_format),
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "issuer": "ABC Corporation",
    "face_value": 2000.0,
    "yield_rate": 4.0,
    "maturity_date": datetime.strptime('2024-09-30', date_format),
    "date_purchased": datetime.strptime('2023-02-20', date_format),
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "issuer": "XYZ Bank",
    "face_value": 1500.0,
    "yield_rate": 2.8,
    "maturity_date": datetime.strptime('2026-05-15', date_format),
    "date_purchased": datetime.strptime('2023-03-10', date_format),
    "portfolio_id": PortfolioList[2]["id"]
  }
]

for bond in BondList:
  instance = Bond(
    id=bond["id"],
    issuer=bond["issuer"],
    face_value=bond["face_value"],
    yield_rate=bond["yield_rate"],
    date_purchased=bond["date_purchased"],
    maturity_date=bond["maturity_date"],
    portfolio_id=bond["portfolio_id"]
    )
  session.add(instance)

EstateList = [
  {
    "id": str(uuid.uuid4()),
    "property_type": "Residential",
    "property_name": "Cozy Cottage",
    "value": 250000.0,
    "location": "123 Main St, Anytown",
    "date_purchased": datetime.strptime('2023-01-15', date_format),
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "property_type": "Commercial",
    "property_name": "Office Building",
    "value": 800000.0,
    "location": "456 Elm St, Metropolis",
    "date_purchased": datetime.strptime('2023-02-20', date_format),
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "property_type": "Residential",
    "property_name": "Beachfront Villa",
    "value": 3500000.0,
    "location": "789 Ocean Dr, Paradise City",
    "date_purchased": datetime.strptime('2023-03-10', date_format),
    "portfolio_id": PortfolioList[2]["id"]
  }
]

for estate in EstateList:
  instance = RealEstate(
    id=estate["id"],
    property_type=estate["property_type"],
    property_name=estate["property_name"],
    value=estate["value"],
    location=estate["location"],
    date_purchased=estate["date_purchased"],
    portfolio_id=estate["portfolio_id"]
    )
  session.add(instance)

EtfList = [
  {
    "id": str(uuid.uuid4()),
    "symbol": 'SPY',
    "fund_name": 'SPDR S&P 500 ETF Trust',
    "price": 450.0,
    "date_purchased": datetime.strptime('2023-01-15', date_format),
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "symbol": 'QQQ',
    "fund_name": 'Invesco QQQ Trust',
    "price": 370.0,
    "date_purchased": datetime.strptime('2023-02-20', date_format),
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "symbol": 'IWM',
    "fund_name": 'iShares Russell 2000 ETF',
    "price": 230.0,
    "date_purchased": datetime.strptime('2023-03-10', date_format),
    "portfolio_id": PortfolioList[2]["id"]
  }
]

for etf in EtfList:
  instance = ETF(
    id=etf["id"],
    symbol=etf["symbol"],
    fund_name=etf["fund_name"],
    price=etf["price"],
    date_purchased=etf["date_purchased"],
    portfolio_id=etf["portfolio_id"]
    )
  session.add(instance)

AccountsList = [
  {
    "id": str(uuid.uuid4()),
    "account_name": "Savings Account",
    "account_type": "Savings",
    "balance": 10000.0,
    "currency": "USD",
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "account_name": "Checking Account",
    "account_type": "Checking",
    "balance": 5000.0,
    "currency": "USD",
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "id": str(uuid.uuid4()),
    "account_name": "Emergency Fund",
    "account_type": "Savings",
    "balance": 15000.0,
    "currency": "USD",
    "portfolio_id": PortfolioList[2]["id"]
  }
]

for account in AccountsList:
  instance = CashAccount(
    id=account["id"],
    account_name=account["account_name"],
    account_type=account["account_type"],
    balance=account["balance"],
    currency=account["currency"],
    portfolio_id=account["portfolio_id"]
    )
  session.add(instance)

session.commit()