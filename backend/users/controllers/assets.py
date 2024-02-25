from flask import Blueprint, abort, jsonify, make_response, request
from marshmallow import ValidationError
from datetime import date
from models.engine import session
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
from services.assets_serializer import *

assets = Blueprint('assets', __name__)

@assets.route('/stocks', methods=['POST', 'DELETE'])
def handle_stock():
    if request.method == 'POST':
        try:
            # Load and validate incoming JSON data using the StockSchema
            stock_data = StockSchema().load(request.get_json())
        except ValidationError as err:
            abort(400, description=err.messages)
        
        # Get the user id from the request
        user_id = request.args.get('user_id')
        if not user_id:
            abort(400, description="User ID is required")

        try:
            # Get the portfolio id associated with the user
            portfolio = session.query(Portfolio).filter(Portfolio.user_id == user_id).one_or_none()
            if not portfolio:
                abort(404, description="Portfolio not found")

            # Set the portfolio id to the stock data
            stock_data['portfolio_id'] = portfolio.id

            # Create and add the stock to the database
            stock = Stock(**stock_data, date_purchased=date.today())
            session.add(stock)
            session.commit()

            return make_response(jsonify(stock.to_dict()), 201)
        except Exception as e:
            abort(500, description=str(e))
    elif request.method == 'DELETE':
        stock_id = request.args.get('id')
        if not stock_id:
            abort(400, description="Stock ID is required")

        # Query the stock to delete
        stock = session.query(Stock).filter_by(id=stock_id).first()
        if not stock:
            abort(404, description="Stock not found")

        # Delete the stock
        session.delete(stock)
        session.commit()

        return make_response(jsonify({"message": "Stock deleted successfully"}), 200)

# Route for adding or deleting a bond
@assets.route('/bonds', methods=['POST', 'DELETE'])
def handle_bond():
    if request.method == 'POST':
        try:
            # Load and validate incoming JSON data using the BondSchema
            bond_data = BondSchema().load(request.get_json())
        except ValidationError as err:
            abort(400, description=err.messages)
        
        # Get the user id from the request
        user_id = request.args.get('user_id')
        if not user_id:
            abort(400, description="User ID is required")

        try:
            # Get the portfolio id associated with the user
            portfolio = session.query(Portfolio).filter(Portfolio.user_id == user_id).one_or_none()
            if not portfolio:
                abort(404, description="Portfolio not found")

            # Set the portfolio id to the bond data
            bond_data['portfolio_id'] = portfolio.id

            # Create and add the bond to the database
            bond = Bond(**bond_data, date_purchased=date.today())
            session.add(bond)
            session.commit()

            return make_response(jsonify(bond.to_dict()), 201)
        except Exception as e:
            abort(500, description=str(e))
    elif request.method == 'DELETE':
        bond_id = request.args.get('id')
        if not bond_id:
            abort(400, description="Bond ID is required")

        # Query the bond to delete
        bond = session.query(Bond).filter_by(id=bond_id).first()
        if not bond:
            abort(404, description="Bond not found")

        # Delete the bond
        session.delete(bond)
        session.commit()

        return make_response(jsonify({"message": "Bond deleted successfully"}), 200)

@assets.route('/real_estate', methods=['POST', 'DELETE'])
def handle_real_estate():
    if request.method == 'POST':
        try:
            # Load and validate incoming JSON data using the RealEstateSchema
            real_estate_data = RealEstateSchema().load(request.get_json())
        except ValidationError as err:
            abort(400, description=err.messages)

        # Get the user id from the request
        user_id = request.args.get('user_id')
        if not user_id:
            abort(400, description="User ID is required")

        try:
            # Get the portfolio id associated with the user
            portfolio = session.query(Portfolio).filter(Portfolio.user_id == user_id).one_or_none()
            if not portfolio:
                abort(404, description="Portfolio not found")

            # Set the portfolio id to the real estate data
            real_estate_data['portfolio_id'] = portfolio.id

            # Create and add the real estate property to the database
            real_estate = RealEstate(**real_estate_data, date_purchased=date.today())
            session.add(real_estate)
            session.commit()

            return make_response(jsonify(real_estate.to_dict()), 201)
        except Exception as e:
            abort(500, description=str(e))
    elif request.method == 'DELETE':
        real_estate_id = request.args.get('id')
        if not real_estate_id:
            abort(400, description="Real Estate ID is required")

        # Query the real estate property to delete
        real_estate = session.query(RealEstate).filter_by(id=real_estate_id).first()
        if not real_estate:
            abort(404, description="Real Estate property not found")

        # Delete the real estate property
        session.delete(real_estate)
        session.commit()

        return make_response(jsonify({"message": "Real Estate property deleted successfully"}), 200)

@assets.route('/cash_accounts', methods=['POST', 'DELETE'])
def handle_cash_account():
    if request.method == 'POST':
        try:
            # Load and validate incoming JSON data using the CashAccountSchema
            cash_account_data = CashAccountSchema().load(request.get_json())
        except ValidationError as err:
            abort(400, description=err.messages)
        
        # Get the user id from the request
        user_id = request.args.get('user_id')
        if not user_id:
            abort(400, description="User ID is required")

        try:
            # Get the portfolio id associated with the user
            portfolio = session.query(Portfolio).filter(Portfolio.user_id == user_id).one_or_none()
            if not portfolio:
                abort(404, description="Portfolio not found")

            # Set the portfolio id to the cash account data
            cash_account_data['portfolio_id'] = portfolio.id

            # Create and add the cash account to the database
            cash_account = CashAccount(**cash_account_data)
            session.add(cash_account)
            session.commit()

            return make_response(jsonify(cash_account.to_dict()), 201)
        except Exception as e:
            abort(500, description=str(e))
    elif request.method == 'DELETE':
        cash_account_id = request.args.get('id')
        if not cash_account_id:
            abort(400, description="Cash account ID is required")

        # Query the cash account to delete
        cash_account = session.query(CashAccount).filter_by(id=cash_account_id).first()
        if not cash_account:
            abort(404, description="Cash account not found")

        # Delete the cash account
        session.delete(cash_account)
        session.commit()

        return make_response(jsonify({"message": "Cash account deleted successfully"}), 200)

@assets.route('/cryptocurrencies', methods=['POST', 'DELETE'])
def handle_cryptocurrency():
    if request.method == 'POST':
        try:
            # Load and validate incoming JSON data using the CryptocurrencySchema
            cryptocurrency_data = CryptocurrencySchema().load(request.get_json())
        except ValidationError as err:
            abort(400, description=err.messages)
        
        # Get the user id from the request
        user_id = request.args.get('user_id')
        if not user_id:
            abort(400, description="User ID is required")

        try:
            # Get the portfolio id associated with the user
            portfolio = session.query(Portfolio).filter(Portfolio.user_id == user_id).one_or_none()
            if not portfolio:
                abort(404, description="Portfolio not found")

            # Set the portfolio id to the cryptocurrency data
            cryptocurrency_data['portfolio_id'] = portfolio.id

            # Create and add the cryptocurrency to the database
            cryptocurrency = Cryptocurrency(**cryptocurrency_data, date_purchased=date.today())
            session.add(cryptocurrency)
            session.commit()

            return make_response(jsonify(cryptocurrency.to_dict()), 201)
        except Exception as e:
            abort(500, description=str(e))
    elif request.method == 'DELETE':
        cryptocurrency_id = request.args.get('id')
        if not cryptocurrency_id:
            abort(400, description="Cryptocurrency ID is required")

        # Query the cryptocurrency to delete
        cryptocurrency = session.query(Cryptocurrency).filter_by(id=cryptocurrency_id).first()
        if not cryptocurrency:
            abort(404, description="Cryptocurrency not found")

        # Delete the cryptocurrency
        session.delete(cryptocurrency)
        session.commit()

        return make_response(jsonify({"message": "Cryptocurrency deleted successfully"}), 200)

@assets.route('/etfs', methods=['POST', 'DELETE'])
def handle_etf():
    if request.method == 'POST':
        try:
            # Load and validate incoming JSON data using the ETFSchema
            etf_data = ETFSchema().load(request.get_json())
        except ValidationError as err:
            abort(400, description=err.messages)
        
        # Get the user id from the request
        user_id = request.args.get('user_id')
        if not user_id:
            abort(400, description="User ID is required")

        try:
            # Get the portfolio id associated with the user
            portfolio = session.query(Portfolio).filter(Portfolio.user_id == user_id).one_or_none()
            if not portfolio:
                abort(404, description="Portfolio not found")

            # Set the portfolio id to the etf data
            etf_data['portfolio_id'] = portfolio.id

            # Create and add the etf to the database
            etf = ETF(**etf_data, date_purchased=date.today())
            session.add(etf)
            session.commit()

            return make_response(jsonify(etf.to_dict()), 201)
        except Exception as e:
            abort(500, description=str(e))
    elif request.method == 'DELETE':
        etf_id = request.args.get('id')
        if not etf_id:
            abort(400, description="ETF ID is required")

        # Query the etf to delete
        etf = session.query(ETF).filter_by(id=etf_id).first()
        if not etf:
            abort(404, description="ETF not found")

        # Delete the etf
        session.delete(etf)
        session.commit()

        return make_response(jsonify({"message": "ETF deleted successfully"}), 200)

@assets.route('/funds', methods=['POST', 'DELETE'])
def handle_fund():
    if request.method == 'POST':
        try:
            # Load and validate incoming JSON data using the FundSchema
            fund_data = FundSchema().load(request.get_json())
        except ValidationError as err:
            abort(400, description=err.messages)
        
        # Get the user id from the request
        user_id = request.args.get('user_id')
        if not user_id:
            abort(400, description="User ID is required")

        try:
            # Get the portfolio id associated with the user
            portfolio = session.query(Portfolio).filter(Portfolio.user_id == user_id).one_or_none()
            if not portfolio:
                abort(404, description="Portfolio not found")

            # Set the portfolio id to the fund data
            fund_data['portfolio_id'] = portfolio.id

            # Create and add the fund to the database
            fund = Fund(**fund_data, date_purchased=date.today())
            session.add(fund)
            session.commit()

            return make_response(jsonify(fund.to_dict()), 201)
        except Exception as e:
            abort(500, description=str(e))
    elif request.method == 'DELETE':
        fund_id = request.args.get('id')
        if not fund_id:
            abort(400, description="Fund ID is required")

        # Query the fund to delete
        fund = session.query(Fund).filter_by(id=fund_id).first()
        if not fund:
            abort(404, description="Fund not found")

        # Delete the fund
        session.delete(fund)
        session.commit()

        return make_response(jsonify({"message": "Fund deleted successfully"}), 200)

@assets.route('/options_derivatives', methods=['POST', 'DELETE'])
def handle_option_derivative():
    if request.method == 'POST':
        try:
            # Load and validate incoming JSON data using the OptionDerivativeSchema
            option_data = OptionsDerivativesSchema().load(request.get_json())
        except ValidationError as err:
            abort(400, description=err.messages)
        
        # Get the user id from the request
        user_id = request.args.get('user_id')
        if not user_id:
            abort(400, description="User ID is required")

        try:
            # Get the portfolio id associated with the user
            portfolio = session.query(Portfolio).filter(Portfolio.user_id == user_id).one_or_none()
            if not portfolio:
                abort(404, description="Portfolio not found")

            # Set the portfolio id to the option data
            option_data['portfolio_id'] = portfolio.id

            # Create and add the option to the database
            option = OptionsDerivatives(**option_data)
            session.add(option)
            session.commit()

            return make_response(jsonify(option.to_dict()), 201)
        except Exception as e:
            abort(500, description=str(e))
    elif request.method == 'DELETE':
        option_id = request.args.get('id')
        if not option_id:
            abort(400, description="Option ID is required")

        # Query the option to delete
        option = session.query(OptionsDerivatives).filter_by(id=option_id).first()
        if not option:
            abort(404, description="Option not found")

        # Delete the option
        session.delete(option)
        session.commit()

        return make_response(jsonify({"message": "Option deleted successfully"}), 200)

@assets.route('/private_equity', methods=['POST', 'DELETE'])
def handle_private_equity():
    if request.method == 'POST':
        try:
            # Load and validate incoming JSON data using the PrivateEquitySchema
            private_equity_data = PrivateEquitySchema().load(request.get_json())
        except ValidationError as err:
            abort(400, description=err.messages)
        
        # Get the user id from the request
        user_id = request.args.get('user_id')
        if not user_id:
            abort(400, description="User ID is required")

        try:
            # Get the portfolio id associated with the user
            portfolio = session.query(Portfolio).filter(Portfolio.user_id == user_id).one_or_none()
            if not portfolio:
                abort(404, description="Portfolio not found")

            # Set the portfolio id to the private equity data
            private_equity_data['portfolio_id'] = portfolio.id

            # Create and add the private equity investment to the database
            private_equity = PrivateEquity(**private_equity_data, date_invested=date.today())
            session.add(private_equity)
            session.commit()

            return make_response(jsonify(private_equity.to_dict()), 201)
        except Exception as e:
            abort(500, description=str(e))
    elif request.method == 'DELETE':
        private_equity_id = request.args.get('id')
        if not private_equity_id:
            abort(400, description="Private Equity ID is required")

        # Query the private equity investment to delete
        private_equity = session.query(PrivateEquity).filter_by(id=private_equity_id).first()
        if not private_equity:
            abort(404, description="Private Equity investment not found")

        # Delete the private equity investment
        session.delete(private_equity)
        session.commit()

        return make_response(jsonify({"message": "Private Equity investment deleted successfully"}))

@assets.route('/reits', methods=['POST', 'DELETE'])
def handle_reits():
    if request.method == 'POST':
        try:
            # Load and validate incoming JSON data using the REITSchema
            reit_data = REITSchema().load(request.get_json())
        except ValidationError as err:
            abort(400, description=err.messages)
        
        # Get the user id from the request
        user_id = request.args.get('user_id')
        if not user_id:
            abort(400, description="User ID is required")

        try:
            # Get the portfolio id associated with the user
            portfolio = session.query(Portfolio).filter(Portfolio.user_id == user_id).one_or_none()
            if not portfolio:
                abort(404, description="Portfolio not found")

            # Set the portfolio id to the REIT data
            reit_data['portfolio_id'] = portfolio.id

            # Create and add the REIT investment to the database
            reit = REIT(**reit_data, date_purchased=date.today())
            session.add(reit)
            session.commit()

            return make_response(jsonify(reit.to_dict()), 201)
        except Exception as e:
            abort(500, description=str(e))
    elif request.method == 'DELETE':
        reit_id = request.args.get('id')
        if not reit_id:
            abort(400, description="REIT ID is required")

        # Query the REIT investment to delete
        reit = session.query(REIT).filter_by(id=reit_id).first()
        if not reit:
            abort(404, description="REIT investment not found")

        # Delete the REIT investment
        session.delete(reit)
        session.commit()

        return make_response(jsonify({"message": "REIT investment deleted successfully"}), 200)