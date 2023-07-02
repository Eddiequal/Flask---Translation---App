from flask import Flask
from flask_login import LoginManager

# APP INSTANCE
app = Flask(__name__)

# SECRET KEY
app.secret_key = 'YOUR_SECRET_KEY'
app.config['LOGIN_VIEW'] = 'login'
# LOGIN SETUP
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'