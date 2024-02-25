from flask import Flask, jsonify
from models.engine import session
from models.portfolio import Portfolio
from services.calculations import *

@app.route('/portfolio/<int:id>')
def get_portfolio(id):
    result = session.query(Portfolio).filter(Portfolio.user_id == id).one_or_none()

    if result:
        current_bond_value = calculate_bond_value(result.bonds)
        current_estate_value = calculate_real_estate_value(result.real_estate)
        current_private_equity_value = calculate_private_equity_value(result.private_equity)
        current_options_value = calculate_options_value(result.options_derivatives)
        current_crypto_value = calculate_crypto_value(result.cryptocurrencies)
        current_cash_value = calculate_cash_value(result.cash_accounts)
        current_equity_value = calculate_equity_value(result.stocks, result.funds, result.etfs, result.reits)

        asset_value_list = [current_equity_value, current_crypto_value, current_bond_value, current_cash_value, current_estate_value, current_options_value, current_private_equity_value]

        assets_owned = sum(asset > 0 for asset in asset_value_list)
        diversity_score = round((assets_owned / len(asset_value_list)) * 100, 2)
        total_value = round(sum(asset_value_list), 2)

        return jsonify({
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
        })

    return jsonify({"error": "Portfolio not found"}), 404