import numpy as np
from datetime import datetime, date

r = 0.05  # Risk-free interest rate (annual)
sigma = 0.2  # Volatility (annual)

def calculate_bond_value(bonds):
    total_value = 0

    for bond in bonds:
      # Calculate the number of periods (t) until maturity
      t = (bond.maturity_date - bond.date_purchased).days / 365.0  # Assuming annual payments
      
      # Convert the yield rate to a decimal
      r = bond.yield_rate / 100.0
      
      # Calculate the current value (PV) of the bond
      PV = (bond.face_value / ((1 + r) ** t))
      
      total_value += PV

    return round(total_value, 2)

def calculate_real_estate_value(estates):
  total_value = 0

  for estate in estates:
    total_value += estate.value

  return round(total_value, 2)


def calculate_private_equity_value(EquityList):
  total_value = 0

  for equity in EquityList:
    total_value += equity.current_value

  return round(total_value, 2)


def black_scholes_call(S, X, T, r, sigma):
    d1 = (np.log(S / X) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    N_d1 = 0.5 * (1 + np.math.erf(d1 / np.sqrt(2)))
    N_d2 = 0.5 * (1 + np.math.erf(d2 / np.sqrt(2)))
    
    call_price = S * N_d1 - X * np.exp(-r * T) * N_d2
    return call_price


def black_scholes_put(S, X, T, r, sigma):
    d1 = (np.log(S / X) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    N_minus_d1 = 0.5 * (1 - np.math.erf(d1 / np.sqrt(2)))
    N_minus_d2 = 0.5 * (1 - np.math.erf(d2 / np.sqrt(2)))
    
    put_price = X * np.exp(-r * T) * N_minus_d2 - S * N_minus_d1
    return put_price

def calculate_options_value(OptionsList):
  total_value = 0

  for option in OptionsList:
    if option.expiration_date > date.today():
      time_to_expiration = (option.expiration_date - date.today()).total_seconds()
      time_to_expiration_years = time_to_expiration / (365.0 * 24 * 60 * 60)
      print(f"TIME TO EXPIRATION: {time_to_expiration_years}")
      if option.contract_type == 'Call':
        total_value += black_scholes_call(option.price, 105, time_to_expiration_years, r, sigma)
      elif option.contract_type == 'Put':
        total_value += black_scholes_put(option.price, 105, time_to_expiration_years, r, sigma)
      
  return round(total_value, 2)

def calculate_crypto_value(CryptoList):
  total_value = 0

  for crypto in CryptoList:
    total_value += crypto.price

  return round(total_value, 2)

def calculate_cash_value(AccountsList):
  total_value = 0

  for account in AccountsList:
    total_value += account.balance

  return round(total_value, 2)

def calculate_equity_value(StocksList, FundList, ETFList, REITList):
  total_value = 0

  for stock in StocksList:
    total_value += (stock.price * stock.quantity)

  for fund in FundList:
    total_value += fund.nav

  for etf in ETFList:
    total_value += etf.price

  for reit in REITList:
    total_value += reit.price_per_share

  return round(total_value, 2)