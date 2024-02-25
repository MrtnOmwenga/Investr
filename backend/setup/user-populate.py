import uuid
import bcrypt
from datetime import datetime

import sys
sys.path.append('C:/Users/Admin/Documents/Portfolio/investr/backend/users')

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
  instance = Users(name=user["name"], email=user["email"], password=user["password"])
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
  instance = Portfolio(user_id=portfolio["user_id"], name=portfolio["name"])
  session.add(instance)


StockList = [
  {
    "symbol": 'AAPL',
    "company_name": 'Apple Inc.',
    "quantity": 200,
    "price": 150.0,
    "date_purchased": datetime.strptime('2023-01-15', date_format),
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "symbol": 'AAPL',
    "company_name": 'Apple Inc.',
    "quantity": 200,
    "price": 150.0,
    "date_purchased": datetime.strptime('2023-01-15', date_format),
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "symbol": 'AAPL',
    "company_name": 'Apple Inc.',
    "quantity": 200,
    "price": 150.0,
    "date_purchased": datetime.strptime('2023-01-15', date_format),
    "portfolio_id": PortfolioList[2]["id"]
  },
  {
    "symbol": 'GOOGL',
    "company_name": 'Alphabet Inc.',
    "quantity": 200,
    "price": 2700.0,
    "date_purchased": datetime.strptime('2023-02-20', date_format),
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "symbol": 'GOOGL',
    "company_name": 'Alphabet Inc.',
    "quantity": 200,
    "price": 2700.0,
    "date_purchased": datetime.strptime('2023-02-20', date_format),
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "symbol": 'GOOGL',
    "company_name": 'Alphabet Inc.',
    "quantity": 200,
    "price": 2700.0,
    "date_purchased": datetime.strptime('2023-02-20', date_format),
    "portfolio_id": PortfolioList[2]["id"]
  },
  {
    "symbol": 'MSFT',
    "company_name": 'Microsoft Corporation',
    "quantity": 200,
    "price": 290.0,
    "date_purchased": datetime.strptime('2023-03-10', date_format),
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "symbol": 'MSFT',
    "company_name": 'Microsoft Corporation',
    "quantity": 200,
    "price": 290.0,
    "date_purchased": datetime.strptime('2023-03-10', date_format),
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
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
    "fund_name": 'Vanguard 500 Index Fund',
    "symbol": 'VFIAX',
    "nav": 342.67,  # NAV as of a specific date
    "date_purchased": datetime.strptime('2023-01-15', '%Y-%m-%d'),  # Date purchased
    "portfolio_id": PortfolioList[0]["id"],  # Portfolio ID
    "fund_type": 'Index Fund'
  },
  {
    "fund_name": 'Fidelity Total Market Index Fund',
    "symbol": 'FSKAX',
    "nav": 112.45,  
    "date_purchased": datetime.strptime('2023-02-20', '%Y-%m-%d'),  
    "portfolio_id": PortfolioList[1]["id"],  
    "fund_type": 'Index Fund'
  },
  {
    "fund_name": 'PIMCO Total Return Fund',
    "symbol": 'PTTAX',
    "nav": 10.50,  
    "date_purchased": datetime.strptime('2023-03-10', '%Y-%m-%d'),  
    "portfolio_id": PortfolioList[2]["id"],  
    "fund_type": 'Mutual Fund'
  }
]

for fund in FundList:
  instance = Fund(
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
    "property_name": 'Sample REIT 1',
    "symbol": 'REIT1',
    "price_per_share": 75.0,
    "date_purchased": datetime.strptime('2023-01-15', date_format),
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "property_name": 'Sample REIT 2',
    "symbol": 'REIT2',
    "price_per_share": 90.0,
    "date_purchased": datetime.strptime('2023-02-20', date_format),
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "property_name": 'Sample REIT 3',
    "symbol": 'REIT3',
    "price_per_share": 80.0,
    "date_purchased": datetime.strptime('2023-03-10', date_format),
    "portfolio_id": PortfolioList[2]["id"]
  }
]

for reit in ReitList:
  instance = REIT(
    property_name=reit["property_name"],
    symbol=reit["symbol"],
    price_per_share=reit["price_per_share"],
    date_purchased=reit["date_purchased"],
    portfolio_id=reit["portfolio_id"]
    )
  session.add(instance)

OptionsList = [
  {
    "contract_name": 'AAPL Call Option',
    "underlying_asset": 'AAPL',
    "contract_type": 'Call',
    "expiration_date": datetime.strptime('2027-05-15', '%Y-%m-%d'),
    "price": 10.0,
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "contract_name": 'AAPL Call Option',
    "underlying_asset": 'AAPL',
    "contract_type": 'Call',
    "expiration_date": datetime.strptime('2027-05-15', '%Y-%m-%d'),
    "price": 10.0,
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "contract_name": 'AAPL Call Option',
    "underlying_asset": 'AAPL',
    "contract_type": 'Call',
    "expiration_date": datetime.strptime('2027-05-15', '%Y-%m-%d'),
    "price": 10.0,
    "portfolio_id": PortfolioList[2]["id"]
  },
  {
    "contract_name": 'GOOGL Put Option',
    "underlying_asset": 'GOOGL',
    "contract_type": 'Put',
    "expiration_date": datetime.strptime('2027-06-20', '%Y-%m-%d'),
    "price": 12.0,
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "contract_name": 'GOOGL Put Option',
    "underlying_asset": 'GOOGL',
    "contract_type": 'Put',
    "expiration_date": datetime.strptime('2027-06-20', '%Y-%m-%d'),
    "price": 12.0,
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "contract_name": 'GOOGL Put Option',
    "underlying_asset": 'GOOGL',
    "contract_type": 'Put',
    "expiration_date": datetime.strptime('2027-06-20', '%Y-%m-%d'),
    "price": 12.0,
    "portfolio_id": PortfolioList[2]["id"]
  },
  {
    "contract_name": 'MSFT Call Option',
    "underlying_asset": 'MSFT',
    "contract_type": 'Call',
    "expiration_date": datetime.strptime('2027-07-10', '%Y-%m-%d'),
    "price": 8.0,
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "contract_name": 'MSFT Call Option',
    "underlying_asset": 'MSFT',
    "contract_type": 'Call',
    "expiration_date": datetime.strptime('2027-07-10', '%Y-%m-%d'),
    "price": 8.0,
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "contract_name": 'MSFT Call Option',
    "underlying_asset": 'MSFT',
    "contract_type": 'Call',
    "expiration_date": datetime.strptime('2027-07-10', '%Y-%m-%d'),
    "price": 8.0,
    "portfolio_id": PortfolioList[2]["id"]
  }
]

for option in OptionsList:
  instance = OptionsDerivatives(
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
    "name": 'Bitcoin',
    "symbol": 'BTC',
    "quantity": 200,
    "price": 45000.0,
    "date_purchased": datetime.strptime('2023-01-15', date_format),
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "name": 'Bitcoin',
    "symbol": 'BTC',
    "quantity": 200,
    "price": 45000.0,
    "date_purchased": datetime.strptime('2023-01-15', date_format),
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "name": 'Bitcoin',
    "symbol": 'BTC',
    "quantity": 200,
    "price": 45000.0,
    "date_purchased": datetime.strptime('2023-01-15', date_format),
    "portfolio_id": PortfolioList[2]["id"]
  },
  {
    "name": 'Ethereum',
    "symbol": 'ETH',
    "quantity": 200,
    "price": 3000.0,
    "date_purchased": datetime.strptime('2023-02-20', date_format),
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "name": 'Ethereum',
    "symbol": 'ETH',
    "quantity": 200,
    "price": 3000.0,
    "date_purchased": datetime.strptime('2023-02-20', date_format),
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "name": 'Ethereum',
    "symbol": 'ETH',
    "quantity": 200,
    "price": 3000.0,
    "date_purchased": datetime.strptime('2023-02-20', date_format),
    "portfolio_id": PortfolioList[2]["id"]
  },
  {
    "name": 'Litecoin',
    "symbol": 'LTC',
    "quantity": 200,
    "price": 150.0,
    "date_purchased": datetime.strptime('2023-03-10', date_format),
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "name": 'Litecoin',
    "symbol": 'LTC',
    "quantity": 200,
    "price": 150.0,
    "date_purchased": datetime.strptime('2023-03-10', date_format),
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "name": 'Litecoin',
    "symbol": 'LTC',
    "quantity": 200,
    "price": 150.0,
    "date_purchased": datetime.strptime('2023-03-10', date_format),
    "portfolio_id": PortfolioList[2]["id"]
  }
]

for crypto in CryptoList:
  instance = Cryptocurrency(
    name=crypto["name"],
    symbol=crypto["symbol"],
    quantity=crypto["quantity"],
    price=crypto["price"],
    date_purchased=crypto["date_purchased"],
    portfolio_id=crypto["portfolio_id"]
    )
  session.add(instance)

EquityList = [
  {
    "equity_name": 'Apple Inc.',
    "date_purchased": datetime.strptime('2023-01-15', '%Y-%m-%d'),
    "commitment_amount": 50000.0,
    "current_value": 55000.0,
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "equity_name": 'Microsoft Corporation',
    "date_purchased": datetime.strptime('2023-02-20', '%Y-%m-%d'),
    "commitment_amount": 75000.0,
    "current_value": 80000.0,
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "equity_name": 'Amazon.com Inc.',
    "date_purchased": datetime.strptime('2023-03-10', '%Y-%m-%d'),
    "commitment_amount": 60000.0,
    "current_value": 63000.0,
    "portfolio_id": PortfolioList[2]["id"]
  }
]

for equity in EquityList:
  instance = PrivateEquity(
    fund_name=equity["equity_name"],
    date_invested=equity["date_purchased"],
    commitment_amount=equity["commitment_amount"],
    current_value=equity["current_value"],
    portfolio_id=equity["portfolio_id"]
  )
  session.add(instance)


BondList = [
  {
    "issuer": "Government of XYZ",
    "face_value": 1000.0,
    "yield_rate": 3.5,
    "maturity_date": datetime.strptime('2025-12-31', date_format),
    "date_purchased": datetime.strptime('2023-01-15', date_format),
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "issuer": "ABC Corporation",
    "face_value": 2000.0,
    "yield_rate": 4.0,
    "maturity_date": datetime.strptime('2024-09-30', date_format),
    "date_purchased": datetime.strptime('2023-02-20', date_format),
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
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
    "property_type": "Residential",
    "property_name": "Cozy Cottage",
    "value": 250000.0,
    "location": "123 Main St, Anytown",
    "date_purchased": datetime.strptime('2023-01-15', date_format),
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "property_type": "Commercial",
    "property_name": "Office Building",
    "value": 800000.0,
    "location": "456 Elm St, Metropolis",
    "date_purchased": datetime.strptime('2023-02-20', date_format),
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
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
    "symbol": 'SPY',
    "fund_name": 'SPDR S&P 500 ETF Trust',
    "price": 450.0,
    "date_purchased": datetime.strptime('2023-01-15', date_format),
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "symbol": 'QQQ',
    "fund_name": 'Invesco QQQ Trust',
    "price": 370.0,
    "date_purchased": datetime.strptime('2023-02-20', date_format),
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "symbol": 'IWM',
    "fund_name": 'iShares Russell 2000 ETF',
    "price": 230.0,
    "date_purchased": datetime.strptime('2023-03-10', date_format),
    "portfolio_id": PortfolioList[2]["id"]
  }
]

for etf in EtfList:
  instance = ETF(
    symbol=etf["symbol"],
    fund_name=etf["fund_name"],
    price=etf["price"],
    date_purchased=etf["date_purchased"],
    portfolio_id=etf["portfolio_id"]
    )
  session.add(instance)

AccountsList = [
  {
    "account_name": "Savings Account",
    "account_type": "Savings",
    "balance": 10000.0,
    "currency": "USD",
    "portfolio_id": PortfolioList[0]["id"]
  },
  {
    "account_name": "Checking Account",
    "account_type": "Checking",
    "balance": 5000.0,
    "currency": "USD",
    "portfolio_id": PortfolioList[1]["id"]
  },
  {
    "account_name": "Emergency Fund",
    "account_type": "Savings",
    "balance": 15000.0,
    "currency": "USD",
    "portfolio_id": PortfolioList[2]["id"]
  }
]

for account in AccountsList:
  instance = CashAccount(
    account_name=account["account_name"],
    account_type=account["account_type"],
    balance=account["balance"],
    currency=account["currency"],
    portfolio_id=account["portfolio_id"]
    )
  session.add(instance)

session.commit()