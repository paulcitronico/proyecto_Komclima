from flask import Blueprint, render_template

index = Blueprint("index",__name__)

@index.route("/")
def index():
    return render_template("index.html")

@index.route("/recoverPassword")
def recoverPassword():
    return render_template("recoverPassword.html")