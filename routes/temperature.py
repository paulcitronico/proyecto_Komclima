from flask import Blueprint, jsonify
from flask_login import login_required
from models.Registro_temperatura import Registro_temperatura

temperature = Blueprint("temperature",__name__)

@temperature.route("/temperatura_promedio")
@login_required
def get_temperatura_promedio():
    data = []
    temp = Registro_temperatura()
    for t in temp.get_data():
        data.append({
            "id": t.id,
            "Fecha": t.Fecha,
            "Temperatura_Promedio": t.Temperatura_Promedio
        })
    return jsonify(data)