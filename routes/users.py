from flask import Blueprint, make_response, request
from models.User import User

users = Blueprint("users",__name__)

@users.route("/register",methods=["POST"])
def register_user():
    headers = {"Content-Type": "text/plain"}

    params = {
        "name": request.form.get("name"),
        "email": request.form.get("email"),
        "password": request.form.get("password"),
        "rut": request.form.get("rut"),
        "type": request.form.get("type")
    }

    user = User(**params)
    if user.search_user(params["rut"])==0:
        user.register_user()
        return make_response("Ok",200,headers)
    return make_response("Error",200,headers)