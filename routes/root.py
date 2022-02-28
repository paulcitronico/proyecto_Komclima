from flask import Blueprint, render_template
from models.Forms.LoginForm import LoginForm

root = Blueprint("root",__name__)

@root.route("/")
def index():
    return render_template("index.html", css="index.css", form=LoginForm())

@root.route("/profile")
def profile_user():
    return render_template("profile.html", css="index.css")