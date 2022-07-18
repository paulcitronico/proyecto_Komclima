from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from models.user import User

user_settings = Blueprint("user_settings",__name__)

@user_settings.route("/name", methods=["POST"])
@login_required
def update_name():
    data = request.get_json()
    res = {}
    user = User.get_by_id(current_user.id)
    user.Name = data["name"]
    user.save()
    res["message"] = "Nombre actualizado con éxito"
    return jsonify(res)

@user_settings.route("/email", methods=["POST"])
@login_required
def update_email():
    data = request.get_json()
    res = {}
    if (User.query.filter_by(Email=data["email"]).first() == None):
        user = User.get_by_id(current_user.id)
        user.Email = data["email"]
        user.save()
        res["message"] = "Email actualizado con éxito"
        res["ok"] = True
    else:
        res["message"] = "Ya existe un correo asociado a otra cuenta"
        res["ok"] = False
    return jsonify(res)

@user_settings.route("/password", methods=["POST"])
@login_required
def update_password():
    data = request.get_json()
    res = {}

    print(current_user.id)
    user = User.get_by_id(current_user.id)

    check_password = user.check_password(data["current_password"])

    if check_password:
        user.set_password(data["new_password"])
        user.save()
        res["message"] = "Contraseña actualizada con éxito"
        res["ok"] = True
    else:
        res["message"] = "Error al actualizar la contraseña"
        res["ok"] = False
    
    return jsonify(res)