from flask import Blueprint, request
from models.service_panel import service_panel as sp

service_panel = Blueprint("service_panel",__name__)

@service_panel.route("/add-parameters",methods=["POST"])
def _add_data():
    data = request.get_json()
    print(data)
    parameters = sp(data["t-max"],data["t-min"],data["h-max"],data["h-min"],data["co2-max"],data["co2-min"])
    parameters.save()
    return "Éxito", 200, {"Content-Type": "text/plain"}
