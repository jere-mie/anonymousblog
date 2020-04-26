from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '79efe2f763efd0ec71a67bc584e47d50'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

from blog import routes