# app/__init__.py

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a strong, secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_db_user:your_db_password@localhost/your_db_name'  # Update with your database URI

db = SQLAlchemy(app)
login_manager = LoginManager(app)
