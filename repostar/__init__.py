from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_object('repostar.config')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from repostar.routes import *
from repostar.models import *
