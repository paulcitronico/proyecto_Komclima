from flask import Blueprint, render_template
from flask_login import login_required

dashboard = Blueprint("dashboard",__name__)

# Ajustes del usuario

# Visión general

# Panel de servicio

# Ajustes de la cuenta del usuario
@dashboard.route("/account")
@login_required
def my_account():
    return render_template("account.html",css="css/account.css")