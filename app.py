from flask import Flask
from routes.root import root
from routes.auth import auth
from routes.temperature import temperature
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models.user import User

app = Flask(__name__)
login_manager = LoginManager()
login_manager.login_view = "root.index"
login_manager.login_message = "Para acceder a esta ruta, necesita autenticarse."

app.config["SECRET_KEY"] = "xjhUgSDQd02ceb4PY3CZ"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{}:{}@{}/{}".format("admin","administrador","localhost","login_example")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

login_manager.init_app(app)
SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    return "No tiene permisos para acceder a esta ruta"

app.register_blueprint(root)
app.register_blueprint(auth)
app.register_blueprint(temperature)