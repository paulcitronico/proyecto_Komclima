from flask import Blueprint, render_template

root = Blueprint("root", __name__)

@root.route("/")
def index():
    return render_template("index.html")

@root.route("/recoverPassword")
def recoverPassword():
    return render_template("recoverPassword.html")