from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI_0, SQLALCHEMY_TRACK_MODIFICATIONS



app = Flask(__name__, static_url_path='',
            static_folder="static",
            template_folder="templates")
app.config.from_object('config')

db = SQLAlchemy(app)

