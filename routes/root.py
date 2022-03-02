from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user
from models.Forms.LoginForm import LoginForm

root = Blueprint("root",__name__)

@root.route("/")
def index():
    if current_user.is_authenticated:
        return redirect("profile")

    return render_template("index.html", css="index.css", form=LoginForm())

@root.route("/profile")
@login_required
def profile_user():
    return render_template("profile.html", css="index.css")