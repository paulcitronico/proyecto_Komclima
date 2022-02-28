from flask import Flask
from routes.root import root
from routes.auth import auth
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models.user import User

app = Flask(__name__)
login_manager = LoginManager()
login_manager.login_view = "root.index"

app.config["SECRET_KEY"] = "34a0ac3ff0f2da8c4776b46619bbdfa7b8736263a3601234cf20c1a7d2064879"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://admin:administrador@localhost/login_example"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

login_manager.init_app(app)
SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

app.register_blueprint(root)
app.register_blueprint(auth)