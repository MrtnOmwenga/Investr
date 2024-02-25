import sys
sys.path.append('C:/Users/Admin/Documents/Portfolio/investr/backend/users')

import unittest
from flask import json
from datetime import date, datetime
from sqlalchemy.orm import sessionmaker
from models import Base
from models.engine import engine
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

from index import app

Session = sessionmaker(bind=engine)


class TestHandleStockEndpoint(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        Base.metadata.create_all(engine)

    def tearDown(self):
        Base.metadata.drop_all(engine)

    def test_add_stock_success(self):
        with Session() as session:
            # Create a test user and portfolio
            user = Users(name='Test User', email='test@example.com', password='password')
            session.add(user)
            session.commit()
            portfolio = Portfolio(name='Test Portfolio', user_id=user.id)
            session.add(portfolio)
            session.commit()

            # Create test stock data
            stock_data = {
                'symbol': 'AAPL',
                'company_name': 'Apple Inc.',
                'quantity': 100,
                'price': 150.25,
            }

            # Send POST request to add stock
            response = self.app.post(f'/api/assets/stocks?user_id={user.id}', json=stock_data)
            self.assertEqual(response.status_code, 201)

            # Check if stock was added to the database
            stock = session.query(Stock).filter_by(symbol='AAPL').first()
            self.assertIsNotNone(stock)
            self.assertEqual(stock.quantity, 100)
            self.assertEqual(stock.price, 150.25)

    def test_add_stock_missing_user_id(self):
        # Send POST request without user_id
        response = self.app.post('/api/assets/stocks', json={})
        self.assertEqual(response.status_code, 400)

    def test_add_stock_invalid_data(self):
        # Send POST request with invalid data
        response = self.app.post('/api/assets/stocks?user_id=test_user', json={'symbol': 'AAPL', 'price': 'invalid'})
        self.assertEqual(response.status_code, 400)

    def test_delete_stock_success(self):
        with Session() as session:
            # Create a test stock
            stock = Stock(symbol='AAPL', company_name='Apple Inc.', quantity=100, price=150.25, date_purchased=date.today(), portfolio_id='string')
            session.add(stock)
            session.commit()

            # Send DELETE request to delete stock
            response = self.app.delete(f'/api/assets/stocks?id={stock.id}')
            self.assertEqual(response.status_code, 200)

            # Check if stock was deleted from the database
            stock = session.query(Stock).filter_by(id='test_stock').first()
            self.assertIsNone(stock)

    def test_delete_stock_missing_id(self):
        # Send DELETE request without stock id
        response = self.app.delete('/api/assets/stocks')
        self.assertEqual(response.status_code, 400)

    def test_delete_nonexistent_stock(self):
        # Send DELETE request with non-existent stock id
        response = self.app.delete('/api/assets/stocks?id=nonexistent')
        self.assertEqual(response.status_code, 404)

class TestHandleBondEndpoint(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        Base.metadata.create_all(engine)

    def tearDown(self):
        Base.metadata.drop_all(engine)

    def test_add_bond_success(self):
        with Session() as session:
            # Create a test user and portfolio
            user = Users(name='Test User', email='test@example.com', password='password')
            session.add(user)
            session.commit()
            portfolio = Portfolio(name='Test Portfolio', user_id=user.id)
            session.add(portfolio)
            session.commit()

            # Create test bond data
            bond_data = {
                'issuer': 'Government',
                'face_value': 1000,
                'yield_rate': 5.5,
                'maturity_date': '2025-02-28'
            }

            # Send POST request to add bond
            response = self.app.post(f'/api/assets/bonds?user_id={user.id}', json=bond_data)
            self.assertEqual(response.status_code, 201)

            # Check if bond was added to the database
            bond = session.query(Bond).filter_by(issuer='Government').first()
            self.assertIsNotNone(bond)
            self.assertEqual(bond.face_value, 1000)
            self.assertEqual(bond.yield_rate, 5.5)

    def test_add_bond_missing_user_id(self):
        # Send POST request without user_id
        response = self.app.post('/api/assets/bonds', json={})
        self.assertEqual(response.status_code, 400)

    def test_add_bond_invalid_data(self):
        # Send POST request with invalid data
        response = self.app.post('/api/assets/bonds?user_id=test_user', json={'issuer': 'Government', 'face_value': 'invalid'})
        self.assertEqual(response.status_code, 400)

    def test_delete_bond_success(self):
        with Session() as session:
            # Create a test bond
            maturity_date = datetime.strptime('2025-02-28', '%Y-%m-%d').date()
            bond = Bond(issuer='Government', face_value=1000, yield_rate=5.5, maturity_date=maturity_date, date_purchased=date.today(), portfolio_id='string')
            session.add(bond)
            session.commit()

            # Send DELETE request to delete bond
            response = self.app.delete(f'/api/assets/bonds?id={bond.id}')
            self.assertEqual(response.status_code, 200)

            # Check if bond was deleted from the database
            bond = session.query(Bond).filter_by(id='test_bond').first()
            self.assertIsNone(bond)

    def test_delete_bond_missing_id(self):
        # Send DELETE request without bond id
        response = self.app.delete('/api/assets/bonds')
        self.assertEqual(response.status_code, 400)

    def test_delete_nonexistent_bond(self):
        # Send DELETE request with non-existent bond id
        response = self.app.delete('/api/assets/bonds?id=nonexistent')
        self.assertEqual(response.status_code, 404)

class TestHandleRealEstateEndpoint(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        Base.metadata.create_all(engine)

    def tearDown(self):
        Base.metadata.drop_all(engine)

    def test_add_real_estate_success(self):
      with Session() as session:
            # Create a test user and portfolio
            user = Users(name='Test User', email='test@example.com', password='password')
            session.add(user)
            session.commit()
            portfolio = Portfolio(name='Test Portfolio', user_id=user.id)
            session.add(portfolio)
            session.commit()
            
            # Create test real estate data
            real_estate_data = {
                  'property_name': 'Test Property',
                  'property_type': 'Residential',
                  'value': 500000,
                  'location': 'Test Location'
            }

            # Send POST request to add real estate
            response = self.app.post(f'/api/assets/real_estate?user_id={user.id}', json=real_estate_data)
            self.assertEqual(response.status_code, 201)

            # Check if real estate was added to the database
            real_estate = session.query(RealEstate).filter_by(property_name='Test Property').first()
            self.assertIsNotNone(real_estate)
            self.assertEqual(real_estate.value, 500000)
            self.assertEqual(real_estate.location, 'Test Location')

    def test_add_real_estate_missing_user_id(self):
        # Send POST request without user_id
        response = self.app.post('/api/assets/real_estate', json={})
        self.assertEqual(response.status_code, 400)

    def test_add_real_estate_invalid_data(self):
        # Send POST request with invalid data
        response = self.app.post('/api/assets/real_estate?user_id=test_user', json={'property_name': 'Test Property', 'value': 'invalid'})
        self.assertEqual(response.status_code, 400)

    def test_delete_real_estate_success(self):
      with Session() as session:
            # Create a test real estate property
            real_estate = RealEstate(property_name='Test Property', property_type='Residential', value=500000, location='Test Location', date_purchased=date.today(), portfolio_id='test_portfolio')
            session.add(real_estate)
            session.commit()

            # Send DELETE request to delete real estate
            response = self.app.delete(f'/api/assets/real_estate?id={real_estate.id}')
            self.assertEqual(response.status_code, 200)

            # Check if real estate was deleted from the database
            real_estate = session.query(RealEstate).filter_by(id=real_estate.id).first()
            self.assertIsNone(real_estate)

    def test_delete_real_estate_missing_id(self):
        # Send DELETE request without real estate id
        response = self.app.delete('/api/assets/real_estate')
        self.assertEqual(response.status_code, 400)

    def test_delete_nonexistent_real_estate(self):
        # Send DELETE request with non-existent real estate id
        response = self.app.delete('/api/assets/real_estate?id=nonexistent')
        self.assertEqual(response.status_code, 404)

class TestHandleCashAccountEndpoint(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        Base.metadata.create_all(engine)

    def tearDown(self):
        Base.metadata.drop_all(engine)

    def test_add_cash_account_success(self):
        with Session() as session:
            # Create a test user and portfolio
            user = Users(name='Test User', email='test@example.com', password='password')
            session.add(user)
            session.commit()
            portfolio = Portfolio(name='Test Portfolio', user_id=user.id)
            session.add(portfolio)
            session.commit()
            
            # Create test cash account data
            cash_account_data = {
                  'account_name': 'Test Account',
                  'account_type': 'Savings',
                  'balance': 5000,
                  'currency': 'USD'
            }

            # Send POST request to add cash account
            response = self.app.post(f'/api/assets/cash_accounts?user_id={user.id}', json=cash_account_data)
            self.assertEqual(response.status_code, 201)

            # Check if cash account was added to the database
            cash_account = session.query(CashAccount).filter_by(account_name='Test Account').first()
            self.assertIsNotNone(cash_account)
            self.assertEqual(cash_account.balance, 5000)
            self.assertEqual(cash_account.currency, 'USD')

    def test_add_cash_account_missing_user_id(self):
        # Send POST request without user_id
        response = self.app.post('/api/assets/cash_accounts', json={})
        self.assertEqual(response.status_code, 400)

    def test_add_cash_account_invalid_data(self):
        # Send POST request with invalid data
        response = self.app.post('/api/assets/cash_accounts?user_id=test_user', json={'account_name': 'Test Account', 'balance': 'invalid'})
        self.assertEqual(response.status_code, 400)

    def test_delete_cash_account_success(self):
        with Session() as session:
            # Create a test cash account
            cash_account = CashAccount(account_name='Test Account', account_type='Savings', balance=5000, currency='USD', portfolio_id='test_portfolio')
            session.add(cash_account)
            session.commit()

            # Send DELETE request to delete cash account
            response = self.app.delete(f'/api/assets/cash_accounts?id={cash_account.id}')
            self.assertEqual(response.status_code, 200)

            # Check if cash account was deleted from the database
            cash_account = session.query(CashAccount).filter_by(id=cash_account.id).first()
            self.assertIsNone(cash_account)

    def test_delete_cash_account_missing_id(self):
        # Send DELETE request without cash account id
        response = self.app.delete('/api/assets/cash_accounts')
        self.assertEqual(response.status_code, 400)

    def test_delete_nonexistent_cash_account(self):
        # Send DELETE request with non-existent cash account id
        response = self.app.delete('/api/assets/cash_accounts?id=nonexistent')
        self.assertEqual(response.status_code, 404)

class TestHandleCryptocurrencyEndpoint(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        Base.metadata.create_all(engine)

    def tearDown(self):
        Base.metadata.drop_all(engine)

    def test_add_cryptocurrency_success(self):
        with Session() as session:
            # Create a test user and portfolio
            user = Users(name='Test User', email='test@example.com', password='password')
            session.add(user)
            session.commit()
            portfolio = Portfolio(name='Test Portfolio', user_id=user.id)
            session.add(portfolio)
            session.commit()
            
            # Create test cryptocurrency data
            cryptocurrency_data = {
                  'name': 'Bitcoin',
                  'symbol': 'BTC',
                  'quantity': 2,
                  'price': 45000
            }

            # Send POST request to add cryptocurrency
            response = self.app.post(f'/api/assets/cryptocurrencies?user_id={user.id}', json=cryptocurrency_data)
            self.assertEqual(response.status_code, 201)

            # Check if cryptocurrency was added to the database
            cryptocurrency = session.query(Cryptocurrency).filter_by(name='Bitcoin').first()
            self.assertIsNotNone(cryptocurrency)
            self.assertEqual(cryptocurrency.quantity, 2)
            self.assertEqual(cryptocurrency.price, 45000)

    def test_add_cryptocurrency_missing_user_id(self):
        # Send POST request without user_id
        response = self.app.post('/api/assets/cryptocurrencies', json={})
        self.assertEqual(response.status_code, 400)

    def test_add_cryptocurrency_invalid_data(self):
        # Send POST request with invalid data
        response = self.app.post('/api/assets/cryptocurrencies?user_id=test_user', json={'name': 'Bitcoin', 'price': 'invalid'})
        self.assertEqual(response.status_code, 400)

    def test_delete_cryptocurrency_success(self):
        with Session() as session:
            # Create a test cryptocurrency
            cryptocurrency = Cryptocurrency(name='Bitcoin', symbol='BTC', quantity=2, price=45000, date_purchased=date.today(), portfolio_id='test_portfolio')
            session.add(cryptocurrency)
            session.commit()

            # Send DELETE request to delete cryptocurrency
            response = self.app.delete(f'/api/assets/cryptocurrencies?id={cryptocurrency.id}')
            self.assertEqual(response.status_code, 200)

            # Check if cryptocurrency was deleted from the database
            cryptocurrency = session.query(Cryptocurrency).filter_by(id=cryptocurrency.id).first()
            self.assertIsNone(cryptocurrency)

    def test_delete_cryptocurrency_missing_id(self):
        # Send DELETE request without cryptocurrency id
        response = self.app.delete('/api/assets/cryptocurrencies')
        self.assertEqual(response.status_code, 400)

    def test_delete_nonexistent_cryptocurrency(self):
        # Send DELETE request with non-existent cryptocurrency id
        response = self.app.delete('/api/assets/cryptocurrencies?id=nonexistent')
        self.assertEqual(response.status_code, 404)

class TestHandleETFEndpoint(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        Base.metadata.create_all(engine)

    def tearDown(self):
        Base.metadata.drop_all(engine)

    def test_add_etf_success(self):
        with Session() as session:
            # Create a test user and portfolio
            user = Users(name='Test User', email='test@example.com', password='password')
            session.add(user)
            session.commit()
            portfolio = Portfolio(name='Test Portfolio', user_id=user.id)
            session.add(portfolio)
            session.commit()
            
            # Create test ETF data
            etf_data = {
                  'symbol': 'SPY',
                  'fund_name': 'SPDR S&P 500 ETF Trust',
                  'price': 400.25
            }

            # Send POST request to add ETF
            response = self.app.post(f'/api/assets/etfs?user_id={user.id}', json=etf_data)
            self.assertEqual(response.status_code, 201)

            # Check if ETF was added to the database
            etf = session.query(ETF).filter_by(symbol='SPY').first()
            self.assertIsNotNone(etf)
            self.assertEqual(etf.price, 400.25)

    def test_add_etf_missing_user_id(self):
        # Send POST request without user_id
        response = self.app.post('/api/assets/etfs', json={})
        self.assertEqual(response.status_code, 400)

    def test_add_etf_invalid_data(self):
        # Send POST request with invalid data
        response = self.app.post('/api/assets/etfs?user_id=test_user', json={'symbol': 'SPY', 'price': 'invalid'})
        self.assertEqual(response.status_code, 400)

    def test_delete_etf_success(self):
        with Session() as session:
            # Create a test ETF
            etf = ETF(symbol='SPY', fund_name='SPDR S&P 500 ETF Trust', price=400.25, date_purchased=date.today(), portfolio_id='test_portfolio')
            session.add(etf)
            session.commit()

            # Send DELETE request to delete ETF
            response = self.app.delete(f'/api/assets/etfs?id={etf.id}')
            self.assertEqual(response.status_code, 200)

            # Check if ETF was deleted from the database
            etf = session.query(ETF).filter_by(id=etf.id).first()
            self.assertIsNone(etf)

    def test_delete_etf_missing_id(self):
        # Send DELETE request without ETF id
        response = self.app.delete('/api/assets/etfs')
        self.assertEqual(response.status_code, 400)

    def test_delete_nonexistent_etf(self):
        # Send DELETE request with non-existent ETF id
        response = self.app.delete('/api/assets/etfs?id=nonexistent')
        self.assertEqual(response.status_code, 404)

class TestHandleFundEndpoint(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        Base.metadata.create_all(engine)

    def tearDown(self):
        Base.metadata.drop_all(engine)

    def test_add_fund_success(self):
        with Session() as session:
            # Create a test user and portfolio
            user = Users(name='Test User', email='test@example.com', password='password')
            session.add(user)
            session.commit()
            portfolio = Portfolio(name='Test Portfolio', user_id=user.id)
            session.add(portfolio)
            session.commit()
            
            # Create test fund data
            fund_data = {
                  'fund_name': 'Vanguard Total Stock Market Index Fund',
                  'symbol': 'VTSAX',
                  'nav': 100.50,
                  'fund_type': 'Index Fund'
            }

            # Send POST request to add fund
            response = self.app.post(f'/api/assets/funds?user_id={user.id}', json=fund_data)
            self.assertEqual(response.status_code, 201)

            # Check if fund was added to the database
            fund = session.query(Fund).filter_by(symbol='VTSAX').first()
            self.assertIsNotNone(fund)
            self.assertEqual(fund.nav, 100.50)

    def test_add_fund_missing_user_id(self):
        # Send POST request without user_id
        response = self.app.post('/api/assets/funds', json={})
        self.assertEqual(response.status_code, 400)

    def test_add_fund_invalid_data(self):
        # Send POST request with invalid data
        response = self.app.post('/api/assets/funds?user_id=test_user', json={'fund_name': 'Vanguard Total Stock Market Index Fund', 'nav': 'invalid'})
        self.assertEqual(response.status_code, 400)

    def test_delete_fund_success(self):
        with Session() as session:
            # Create a test fund
            fund = Fund(fund_name='Vanguard Total Stock Market Index Fund', symbol='VTSAX', nav=100.50, date_purchased=date.today(), portfolio_id='test_portfolio', fund_type='Index Fund')
            session.add(fund)
            session.commit()

            # Send DELETE request to delete fund
            response = self.app.delete(f'/api/assets/funds?id={fund.id}')
            self.assertEqual(response.status_code, 200)

            # Check if fund was deleted from the database
            fund = session.query(Fund).filter_by(id=fund.id).first()
            self.assertIsNone(fund)

    def test_delete_fund_missing_id(self):
        # Send DELETE request without fund id
        response = self.app.delete('/api/assets/funds')
        self.assertEqual(response.status_code, 400)

    def test_delete_nonexistent_fund(self):
        # Send DELETE request with non-existent fund id
        response = self.app.delete('/api/assets/funds?id=nonexistent')
        self.assertEqual(response.status_code, 404)

class TestHandleOptionDerivativeEndpoint(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        Base.metadata.create_all(engine)

    def tearDown(self):
        Base.metadata.drop_all(engine)

    def test_add_option_derivative_success(self):
        with Session() as session:
            # Create a test user and portfolio
            user = Users(name='Test User', email='test@example.com', password='password')
            session.add(user)
            session.commit()
            portfolio = Portfolio(name='Test Portfolio', user_id=user.id)
            session.add(portfolio)
            session.commit()
            
            # Create test option data
            option_data = {
                  'contract_name': 'Test Option',
                  'underlying_asset': 'AAPL',
                  'contract_type': 'Call Option',
                  'expiration_date': '2025-02-28',
                  'price': 100.50
            }

            # Send POST request to add option
            response = self.app.post(f'/api/assets/options_derivatives?user_id={user.id}', json=option_data)
            self.assertEqual(response.status_code, 201)

            # Check if option was added to the database
            option = session.query(OptionsDerivatives).filter_by(contract_name='Test Option').first()
            self.assertIsNotNone(option)
            self.assertEqual(option.price, 100.50)

    def test_add_option_derivative_missing_user_id(self):
        # Send POST request without user_id
        response = self.app.post('/api/assets/options_derivatives', json={})
        self.assertEqual(response.status_code, 400)

    def test_add_option_derivative_invalid_data(self):
        # Send POST request with invalid data
        response = self.app.post('/api/assets/options_derivatives?user_id=test_user', json={'contract_name': 'Test Option', 'price': 'invalid'})
        self.assertEqual(response.status_code, 400)

    def test_delete_option_derivative_success(self):
        with Session() as session:
            # Create a test option
            expiration_date = datetime.strptime('2025-02-28', '%Y-%m-%d').date()
            option = OptionsDerivatives(contract_name='Test Option', underlying_asset='AAPL', contract_type='Call Option', expiration_date=expiration_date, price=100.50, portfolio_id='test_portfolio')
            session.add(option)
            session.commit()

            # Send DELETE request to delete option
            response = self.app.delete(f'/api/assets/options_derivatives?id={option.id}')
            self.assertEqual(response.status_code, 200)

            # Check if option was deleted from the database
            option = session.query(OptionsDerivatives).filter_by(id=option.id).first()
            self.assertIsNone(option)

    def test_delete_option_derivative_missing_id(self):
        # Send DELETE request without option id
        response = self.app.delete('/api/assets/options_derivatives')
        self.assertEqual(response.status_code, 400)

    def test_delete_nonexistent_option_derivative(self):
        # Send DELETE request with non-existent option id
        response = self.app.delete('/api/assets/options_derivatives?id=nonexistent')
        self.assertEqual(response.status_code, 404)

class TestHandlePrivateEquityEndpoint(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        Base.metadata.create_all(engine)

    def tearDown(self):
        Base.metadata.drop_all(engine)

    def test_add_private_equity_success(self):
        with Session() as session:
            # Create a test user and portfolio
            user = Users(name='Test User', email='test@example.com', password='password')
            session.add(user)
            session.commit()
            portfolio = Portfolio(name='Test Portfolio', user_id=user.id)
            session.add(portfolio)
            session.commit()
            
            # Create test private equity data
            private_equity_data = {
                  'fund_name': 'Test Fund',
                  'commitment_amount': 100000,
                  'current_value': 120000
            }

            # Send POST request to add private equity
            response = self.app.post(f'/api/assets/private_equity?user_id={user.id}', json=private_equity_data)
            self.assertEqual(response.status_code, 201)

            # Check if private equity was added to the database
            private_equity = session.query(PrivateEquity).filter_by(fund_name='Test Fund').first()
            self.assertIsNotNone(private_equity)
            self.assertEqual(private_equity.commitment_amount, 100000)
            self.assertEqual(private_equity.current_value, 120000)

    def test_add_private_equity_missing_user_id(self):
        # Send POST request without user_id
        response = self.app.post('/api/assets/private_equity', json={})
        self.assertEqual(response.status_code, 400)

    def test_add_private_equity_invalid_data(self):
        # Send POST request with invalid data
        response = self.app.post('/api/assets/private_equity?user_id=test_user', json={'fund_name': 'Test Fund', 'commitment_amount': 'invalid'})
        self.assertEqual(response.status_code, 400)

    def test_delete_private_equity_success(self):
        with Session() as session:
            # Create a test private equity investment
            private_equity = PrivateEquity(fund_name='Test Fund', commitment_amount=100000, current_value=120000, portfolio_id='test_portfolio', date_invested=date.today())
            session.add(private_equity)
            session.commit()

            # Send DELETE request to delete private equity
            response = self.app.delete(f'/api/assets/private_equity?id={private_equity.id}')
            self.assertEqual(response.status_code, 200)

            # Check if private equity was deleted from the database
            private_equity = session.query(PrivateEquity).filter_by(id=private_equity.id).first()
            self.assertIsNone(private_equity)

    def test_delete_private_equity_missing_id(self):
        # Send DELETE request without private equity id
        response = self.app.delete('/api/assets/private_equity')
        self.assertEqual(response.status_code, 400)

    def test_delete_nonexistent_private_equity(self):
        # Send DELETE request with non-existent private equity id
        response = self.app.delete('/api/assets/private_equity?id=nonexistent')
        self.assertEqual(response.status_code, 404)

class TestHandleREITSEndpoint(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        Base.metadata.create_all(engine)

    def tearDown(self):
        Base.metadata.drop_all(engine)

    def test_add_reit_success(self):
        with Session() as session:
            # Create a test user and portfolio
            user = Users(name='Test User', email='test@example.com', password='password')
            session.add(user)
            session.commit()
            portfolio = Portfolio(name='Test Portfolio', user_id=user.id)
            session.add(portfolio)
            session.commit()
            
            # Create test REIT data
            reit_data = {
                  'property_name': 'Test REIT',
                  'symbol': 'REIT',
                  'price_per_share': 50.0
            }

            # Send POST request to add REIT
            response = self.app.post(f'/api/assets/reits?user_id={user.id}', json=reit_data)
            self.assertEqual(response.status_code, 201)

            # Check if REIT was added to the database
            reit = session.query(REIT).filter_by(property_name='Test REIT').first()
            self.assertIsNotNone(reit)
            self.assertEqual(reit.price_per_share, 50.0)

    def test_add_reit_missing_user_id(self):
        # Send POST request without user_id
        response = self.app.post('/api/assets/reits', json={})
        self.assertEqual(response.status_code, 400)

    def test_add_reit_invalid_data(self):
        # Send POST request with invalid data
        response = self.app.post('/api/assets/reits?user_id=test_user', json={'name': 'Test REIT', 'price': 'invalid'})
        self.assertEqual(response.status_code, 400)

    def test_delete_reit_success(self):
        with Session() as session:
            # Create a test REIT investment
            reit = REIT(property_name='Test REIT', symbol='REIT', price_per_share=50.0, portfolio_id='test_portfolio', date_purchased=date.today())
            session.add(reit)
            session.commit()

            # Send DELETE request to delete REIT
            response = self.app.delete(f'/api/assets/reits?id={reit.id}')
            self.assertEqual(response.status_code, 200)

            # Check if REIT was deleted from the database
            reit = session.query(REIT).filter_by(id=reit.id).first()
            self.assertIsNone(reit)

    def test_delete_reit_missing_id(self):
        # Send DELETE request without REIT id
        response = self.app.delete('/api/assets/reits')
        self.assertEqual(response.status_code, 400)

    def test_delete_nonexistent_reit(self):
        # Send DELETE request with non-existent REIT id
        response = self.app.delete('/api/assets/reits?id=nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
