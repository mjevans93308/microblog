from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir


App = Flask(__name__)
App.config.from_object('config')
db = SQLAlchemy(App)

lm = LoginManager()
lm.init_app(App)
lm.login_view = 'login'
oid = OpenID(App, os.path.join(basedir, 'tmp'))

from app import views, models

