from flask import Flask
from routes.root import root
from routes.users import users

# Instanciar Flask
app = Flask(__name__)

# Definir las rutas de la aplicación
app.register_blueprint(root)
app.register_blueprint(users, url_prefix="/users")

if __name__ == "__main__":
    app.run(debug=True,port=5000)