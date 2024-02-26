from flask import Flask, url_for
from views.app import views
from forms.forms import forms
from controllers.users import users

import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

app.register_blueprint(views)
app.register_blueprint(forms, url_prefix="/forms")
app.register_blueprint(users, url_prefix="/api/users")

if __name__ == '__main__':
    app.run(debug=True)