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

from .calc import calculate_bond_value,calculate_real_estate_value, calculate_private_equity_value, calculate_options_value, calculate_crypto_value, calculate_cash_value, calculate_equity_value

def portfolio(id):
  result = session.query(Portfolio).filter(Portfolio.user_id == id).one()

  current_bond_value = calculate_bond_value(result.bonds)
  current_estate_value = calculate_real_estate_value(result.real_estate)
  current_private_equity_value = calculate_private_equity_value(result.private_equity)
  current_options_value = calculate_options_value(result.options_derivatives)
  current_crypto_value = calculate_crypto_value(result.cryptocurrencies)
  current_cash_value = calculate_cash_value(result.cash_accounts)
  current_equity_value = calculate_equity_value(result.stocks, result.funds, result.etfs, result.reits)

  asset_value_list = [current_equity_value, current_crypto_value, current_bond_value, current_cash_value, current_estate_value, current_options_value, current_private_equity_value]

  assets_owned = 0
  for asset in asset_value_list:
    if asset > 0:
      assets_owned += 1

  diversity_score = round((assets_owned / len(asset_value_list)) * 100, 2)
  total_value = round(sum(asset_value_list), 2)

  if result:
    return {
      "name": result.name,
      "id": result.id,
      "user_id": result.user_id,
      "user": result.user,
      "total_value": total_value,
      "diversity_score": diversity_score,
      "Equity-Based-Assets": {
        "total_value": current_equity_value,
        "stocks": result.stocks,
        "funds": result.funds,
        "etfs": result.etfs,
        "reits": result.reits,
      },
      "Fixed-Income-Assets": {
        "total_value": current_bond_value,
        "bonds": result.bonds,
      },
      "Real-Assets": {
        "total_value": current_estate_value,
        "real_estate": result.real_estate,
      },
      "Alternative-Investments": {
        "total_value": current_private_equity_value,
        "private_equity": result.private_equity,
      },
      "Derivative-Investments": {
        "total_value": current_options_value,
        "options_derivatives": result.options_derivatives,
      },
      "Digital-Assets": {
        "total_value": current_crypto_value,
        "cryptocurrencies": result.cryptocurrencies,
      },
      "Liquid-Assets": {
        "total_value": current_cash_value,
        "cash_accounts": result.cash_accounts
      },
    }
  return None