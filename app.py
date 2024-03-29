from flask import Flask, render_template, abort
from routes.root import root
from routes.auth import auth
from routes.dashboard import dashboard
from routes.user_settings import user_settings
from routes.users_manager import users_manager
from routes.service_panel import service_panel
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models.user import User
from utils.error_messages import error as status_code_error
from dotenv import dotenv_values

config = dotenv_values(".env")

app = Flask(__name__)
login_manager = LoginManager()
login_manager.login_view = "root.index"
login_manager.login_message = "Para acceder a esta ruta, necesita autenticarse."

app.config["SECRET_KEY"] = "xjhUgSDQd02ceb4PY3CZ"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{}:{}@{}/{}".format(config["DB_USERNAME"],config["DB_PASSWORD"],config["DB_URL"],config["DB_NAME"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

login_manager.init_app(app)
SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    return abort(401)

@app.errorhandler(401)
def error_401_handler(e):
    return render_template("error.html",css="css/error.css",error=status_code_error["401"]), 401

@app.errorhandler(403)
def error_403_handler(e):
    return render_template("error.html",css="css/error.css",error=status_code_error["403"]), 403

@app.errorhandler(404)
def error_404_handler(e):
    return render_template("error.html",css="css/error.css",error=status_code_error["404"]), 404

app.register_blueprint(root)
app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(service_panel)
app.register_blueprint(user_settings)
app.register_blueprint(users_manager)