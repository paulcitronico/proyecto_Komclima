from utils.db import db

class Registro_temperatura(db.Model):
    __tablename__ = "Registro_temperatura"
    id = db.Column(db.Integer,primary_key=True)
    Fecha = db.Column(db.String(20),nullable=False)
    Temperatura_Promedio = db.Column(db.String(20),nullable=False)

    # Obtener la temperatura promedio (obtiene todos los registros)
    def get_data(self) -> list:
        return db.session.query(Registro_temperatura).all()

    def __repr__(self) -> str:
        return "<Registro_temperatura />"