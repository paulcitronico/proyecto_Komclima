import json
from flask import Blueprint, jsonify, request
from models.user import User

users_manager = Blueprint("users_manager",__name__)

@users_manager.route("/get-users")
def load_users():
    data = []
    users = User.query.all()
    for user in users:
        data.append({
            "id": user.id,
            "name": user.Name,
            "rut": user.Rut,
            "email": user.Email,
            "rol": user.Type
        })
    return jsonify(data)

@users_manager.route("/get-user", methods=["POST", "GET"])
def load_user():
    id_rx = request.get_data()
    user = User.get_by_id(id_rx)
    if (user!=None):
        data = {
            "id": user.id,
            "name": user.Name,
            "rut": user.Rut,
            "email": user.Email,
            "rol": user.Type,
            "error": False
        }
        return jsonify(data)
    return jsonify({"error":True,"message": "Usuario no encontrado"})