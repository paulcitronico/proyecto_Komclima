from app import app
from utils.db import db

with app.app_context():
    db.create_all()

@app.teardown_appcontext
def shutdown_session(exc=None):
    db.session.remove()

if __name__ == "__main__":
    app.run(debug=True)