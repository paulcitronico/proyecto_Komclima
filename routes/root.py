from flask import Blueprint, render_template
from models.Forms.LoginForm import LoginForm

root = Blueprint("root",__name__)

@root.route("/")
def index():
    return render_template("index.html", css="index.css", form=LoginForm())