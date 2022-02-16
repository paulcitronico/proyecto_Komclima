from flask import Flask
from routes.root import root

# Instanciar Flask
app = Flask(__name__)

# Definir las rutas de la aplicación
app.register_blueprint(root)

if __name__ == "__main__":
    app.run(port=4000)