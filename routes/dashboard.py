from flask import Blueprint, render_template
from flask_login import login_required
from routes.decorator import superadmin_required

dashboard = Blueprint("dashboard",__name__)

# Ajustes del usuario

# Visión general
@dashboard.route("/overview")
@login_required
def overview():
    return render_template("overview.html")

# Panel de servicio

# Gestión de usuarios
@dashboard.route("/users")
@login_required
def users_manager():
    return render_template("users-dashboard.html", css="css/user-manager.css")

# Ajustes de la cuenta del usuario
@dashboard.route("/account")
@login_required
def my_account():
    return render_template("account.html",css="css/account.css")