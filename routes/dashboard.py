from flask import Blueprint, render_template
from flask_login import login_required
from routes.decorator import superadmin_required, role_required

dashboard = Blueprint("dashboard",__name__)

# Ajustes del usuario
@dashboard.route("/user-settings")
@login_required
def user_settings():
    return render_template("user-settings.html")

# Visión general
@dashboard.route("/overview")
@login_required
def overview():
    return render_template("overview.html")

# Panel de servicio
@dashboard.route("/service-panel")
@login_required
def service_panel():
    return render_template("service-panel.html")

# Gestión de usuarios
@dashboard.route("/users")
@login_required
@role_required(role=["Superadmin"])
def users_manager():
    return render_template("users-dashboard.html", css="css/user-manager.css")

# Ajustes de la cuenta del usuario
@dashboard.route("/account")
@login_required
def my_account():
    return render_template("account.html",css="css/account.css")