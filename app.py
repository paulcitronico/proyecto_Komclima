from flask import Flask
from routes.index import index

# Instanciar Flask
app = Flask(__name__)

# Definir las rutas de la aplicación
app.register_blueprint(index)

# Levantar o ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True,port=4000)