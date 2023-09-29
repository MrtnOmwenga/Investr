from flask import Blueprint, render_template, Response, request, flash, url_for, redirect, session, g
from .services.data import AddStock, AddBond

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
    return render_template('cash_accounts.html')

@forms.route('/crypto-forms', methods =["GET", "POST"])
def crypto():
    return render_template('cryptocurrencies.html')

@forms.route('/etfs-forms', methods =["GET", "POST"])
def etfs():
    return render_template('etfs.html')

@forms.route('/funds-forms', methods =["GET", "POST"])
def funds():
    return render_template('funds.html')

@forms.route('/options-forms', methods =["GET", "POST"])
def options():
    return render_template('options.html')

@forms.route('/private-equity-forms', methods =["GET", "POST"])
def priavte_equity():
    return render_template('private_equity.html')

@forms.route('/real-estate-forms', methods =["GET", "POST"])
def real_estate():
    return render_template('real_estate.html')

@forms.route('/reits-forms', methods =["GET", "POST"])
def reits():
    return render_template('reits.html')