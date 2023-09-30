from flask import Blueprint, render_template, Response, request, flash, url_for, redirect, session, g
from .services.data import AddStock, DeleteStock, AddBond, DeleteBond, AddProperty, DeleteProperty, AddOption, DeleteOption, AddPrivateEquity, DeletePrivateEquity, AddCrypto, DeleteCrypto, AddAccount, DeleteAccount

forms = Blueprint("forms", __name__,
                  template_folder='forms',
                  static_folder='form-styles',
                  static_url_path='/forms')

@forms.before_request
def before_request():
   g.user = None

   if 'user' in session:
      g.user = session['user']

@forms.route('/stock-forms', methods =["GET", "POST"])
def stocks():
    if g.user:
        if request.method == "POST":
            symbol = request.form.get("symbol")
            name = request.form.get("name")
            quantity = request.form.get("quantity")
            price = request.form.get("purchase_price")

            if not symbol:
                flash('Symbol is required!')
            elif not name:
                flash('Name is required!')
            elif not quantity:
                flash('Quantity is required!')
            elif not price:
                flash('Price is required!')
            else:
                added = AddStock(session['user']["id"], symbol, name, quantity, price)
                if added:
                    redirect(url_for('views.equity_assets'))
        return render_template('stocks.html')
    else:
      return redirect(url_for('views.login'))

@forms.route('/bond-forms', methods =["GET", "POST"])
def bonds():
     if g.user:
        if request.method == "POST":
            issuer = request.form.get("issuer")
            face_value = request.form.get("face_value")
            yield_rate = request.form.get("yield_rate")
            maturity_date = request.form.get("maturity_date")

            if not issuer:
                flash('issuer is required!')
            elif not face_value:
                flash('face_value is required!')
            elif not yield_rate:
                flash('yield_rate is required!')
            elif not maturity_date:
                flash('maturity_date is required!')
            else:
                added = AddBond(session['user']["id"], issuer, face_value, yield_rate, maturity_date)
                if added:
                    redirect(url_for('views.fixed_assets'))
        return render_template('bonds.html')
     else:
         return redirect(url_for('views.login'))

@forms.route('/cash-forms', methods =["GET", "POST"])
def cash():
    if g.user:
        if request.method == "POST":
            account_name = request.form.get("account_name")
            account_type = request.form.get("account_type")
            balance = request.form.get("balance")
            currency = request.form.get("currency")

            if not account_name:
                flash('account_name is required!')
            elif not balance:
                flash('commitment_amount is required!')
            elif not account_type:
                flash('account_type is required!')
            elif not currency:
                flash('currency is required!')
            else:
                added = AddAccount(session['user']["id"], balance, account_name, account_type, currency)
                if added:
                    redirect(url_for('views.liquid_assets'))
        return render_template('cash_accounts.html')
    else:
      return redirect(url_for('views.login'))

@forms.route('/crypto-forms', methods =["GET", "POST"])
def crypto():
    if g.user:
        if request.method == "POST":
            name = request.form.get("name")
            symbol = request.form.get("symbol")
            quantity = request.form.get("quantity")
            price = request.form.get("current_price")

            if not name:
                flash('name is required!')
            elif not symbol:
                flash('symbol is required!')
            elif not quantity:
                flash('quantity is required!')
            elif not price:
                flash('price is required!')
            else:
                added = AddCrypto(session['user']["id"], name, quantity, symbol, price)
                if added:
                    redirect(url_for('views.digital_assets'))
        return render_template('cryptocurrencies.html')
    else:
      return redirect(url_for('views.login'))

@forms.route('/etfs-forms', methods =["GET", "POST"])
def etfs():
    return render_template('etfs.html')

@forms.route('/funds-forms', methods =["GET", "POST"])
def funds():
    return render_template('funds.html')

@forms.route('/options-forms', methods =["GET", "POST"])
def options():
    if g.user:
        if request.method == "POST":
            underlying_asset = request.form.get("underlying_asset")
            contract_type = request.form.get("contract_type")
            contract_name = request.form.get("contract_name")
            expiration_date = request.form.get("expiration_date")
            price = request.form.get("price")

            if not underlying_asset:
                flash('underlying_asset is required!')
            elif not contract_type:
                flash('contract_type is required!')
            elif not contract_name:
                flash('contract_name is required!')
            elif not expiration_date:
                flash('expiration_date is required!')
            elif not price:
                flash('price is required!')
            else:
                added = AddOption(session['user']["id"], underlying_asset, contract_name, contract_type, expiration_date, price)
                if added:
                    redirect(url_for('views.derivative_investments'))
        return render_template('options.html')
    else:
      return redirect(url_for('views.login'))

@forms.route('/private-equity-forms', methods =["GET", "POST"])
def private_equity():
    if g.user:
        if request.method == "POST":
            fund_name = request.form.get("fund_name")
            investment_date = request.form.get("investment_date")
            commitment_amount = request.form.get("commitment_amount")
            current_value = request.form.get("current_value")

            if not fund_name:
                flash('fund_name is required!')
            elif not commitment_amount:
                flash('commitment_amount is required!')
            elif not investment_date:
                flash('investment_date is required!')
            elif not current_value:
                flash('current_value is required!')
            else:
                added = AddPrivateEquity(session['user']["id"], commitment_amount, fund_name, investment_date, current_value)
                if added:
                    redirect(url_for('views.derivative_investments'))
        return render_template('private_equity.html')
    else:
      return redirect(url_for('views.login'))

@forms.route('/real-estate-forms', methods =["GET", "POST"])
def real_estate():
    if g.user:
        if request.method == "POST":
            property_type = request.form.get("property_type")
            property_name = request.form.get("property_name")
            value = request.form.get("value")
            location = request.form.get("location")

            if not property_type:
                flash('property_type is required!')
            elif not property_name:
                flash('property_name is required!')
            elif not value:
                flash('value is required!')
            elif not location:
                flash('location is required!')
            else:
                added = AddProperty(session['user']["id"], property_type, property_name, value, location)
                if added:
                    redirect(url_for('views.real_assets'))
        return render_template('real_estate.html')
    else:
      return redirect(url_for('views.login'))

@forms.route('/reits-forms', methods =["GET", "POST"])
def reits():
    return render_template('reits.html')



@forms.route('/functions/delete-stock/<id>', methods=["POST"])
def delete_stock(id):
    DeleteStock(id)
    return redirect(url_for('views.equity_assets'))

@forms.route('/functions/delete-bond/<id>', methods=["POST"])
def delete_bond(id):
    DeleteBond(id)
    return redirect(url_for('views.fixed_assets'))

@forms.route('/functions/delete-property/<id>', methods=["POST"])
def delete_property(id):
    DeleteProperty(id)
    return redirect(url_for('views.real_assets'))

@forms.route('/functions/delete-option/<id>', methods=["POST"])
def delete_option(id):
    DeleteOption(id)
    return redirect(url_for('views.derivative_investments'))

@forms.route('/functions/delete-private-equity/<id>', methods=["POST"])
def delete_private_equity(id):
    DeletePrivateEquity(id)
    return redirect(url_for('views.alternative_investments'))

@forms.route('/functions/delete-crypto/<id>', methods=["POST"])
def delete_crypto(id):
    DeleteCrypto(id)
    return redirect(url_for('views.digital_assets'))

@forms.route('/functions/delete-account/<id>', methods=["POST"])
def delete_account(id):
    DeleteAccount(id)
    return redirect(url_for('views.liquid_assets'))