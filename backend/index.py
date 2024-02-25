from flask import Flask, url_for
from users.controllers.users import users
from users.controllers.assets import assets

import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

app.register_blueprint(users, url_prefix="/api/users")
app.register_blueprint(assets, url_prefix="/api/assets")

if __name__ == '__main__':
    app.run(debug=True)