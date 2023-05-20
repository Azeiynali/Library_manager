from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Config $ variabels
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../Library.db'
db = SQLAlchemy(app)

from manager.routes import *