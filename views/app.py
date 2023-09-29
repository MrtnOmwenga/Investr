from flask import Blueprint, render_template, Response, request, flash, url_for, redirect, session, g
from .services.user import Login, Register
from .services.portfolio import portfolio


views = Blueprint("views", __name__,
                  template_folder='templates',
                  static_folder='static',
                  static_url_path='/views')

@views.before_request
def before_request():
   g.user = None

   if 'user' in session:
      g.user = session['user']

@views.route("/")
def home():
   return render_template('home.html')

@views.route("/login", methods =["GET", "POST"])
def login():
   if request.method == 'POST':
      session.pop('user', None)
      email = request.form.get("email")
      password = request.form.get("password")

      if not email:
         flash('Name is required!')
      elif not password:
         flash('Password is required!')
      else:
         user = Login(email, password)
         if user is not None:
            session['user'] = user.to_dict()
            return redirect(url_for('views.dashboard'))
         else:
            flash("Invalid username or password")
   return render_template('login.html')

@views.route("/register", methods =["GET", "POST"])
def register():
   if request.method == 'POST':
      name = request.form.get('name')
      email = request.form.get("email")
      password = request.form.get("password")

      if not name:
         flash('Name is required!')
      elif not email:
         flash('Email is required!')
      elif not password:
         flash('Password is required!')
      else:
         user = Register(name, email, password)
         if user is not None:
            return redirect(url_for('views.dashboard'))
   return render_template('register.html')

@views.route('/dashboard')
def dashboard():
   if g.user:
      user = session['user']
      data = portfolio(user["id"])
      return render_template('dashboard.html', data=data)
   else:
      return redirect(url_for('views.login'))

@views.route('/equity-assets')
def equity_assets():
   if g.user:
      user = session['user']
      data = portfolio(user["id"])
      return render_template('equity-assets.html', data=data)
   else:
      return redirect(url_for('views.login'))

@views.route('/fixed-assets')
def fixed_assets():
   if g.user:
      user = session['user']
      data = portfolio(user["id"])
      return render_template('fixed-assets.html', data=data)
   else:
      return redirect(url_for('views.login'))

@views.route('/real-assets')
def real_assets():
   if g.user:
      user = session['user']
      data = portfolio(user["id"])
      return render_template('real-assets.html', data=data)
   else:
      return redirect(url_for('views.login'))

@views.route('/alternative-investments')
def alternative_investments():
   if g.user:
      user = session['user']
      data = portfolio(user["id"])
      return render_template('alternative-investments.html', data=data)
   else:
      return redirect(url_for('views.login'))
   
@views.route('/derivative-investments')
def derivative_investments():
   if g.user:
      user = session['user']
      data = portfolio(user["id"])
      return render_template('derivative-investments.html', data=data)
   else:
      return redirect(url_for('views.login'))

@views.route('/digital-assets')
def digital_assets():
   if g.user:
      user = session['user']
      data = portfolio(user["id"])
      return render_template('digital-assets.html', data=data)
   else:
      return redirect(url_for('views.login'))

@views.route('/liquid-assets')
def liquid_assets():
   if g.user:
      user = session['user']
      data = portfolio(user["id"])
      return render_template('liquid-assets.html', data=data)
   else:
      return redirect(url_for('views.login'))