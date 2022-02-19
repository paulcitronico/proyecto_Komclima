from sqlalchemy import null
from utils.db import con
from werkzeug.security import generate_password_hash, check_password_hash

class User:

    get_user_query = (
        "SELECT * FROM Login WHERE Rut=%s"
    )

    add_user = (
        "INSERT INTO Login "
        "(Name, Password, Rut, Email, Type) "
        "VALUES(%(name)s, %(password)s, %(rut)s, %(email)s, %(type)s)"
    )

    data_user = {
        "name": null,
        "password": null,
        "rut": null,
        "email": null,
        "type": null # Rol
    }

    def __init__(self, **args) -> None:
        self.cursor = con.cursor()
        if len(args)==5: # Para registrar usuarios recibe 5 argumentos (name, password, rut, email, type)
            self.data_user = args
        elif len(args)==0:
            self.data_user = {}

    def register_user(self):
        self.cursor.execute(self.add_user,self.data_user)
        con.commit()
        self.cursor.close()

    def search_user(self, rut):
        self.cursor.execute(self.get_user_query,(rut,))
        result = self.cursor.fetchall()
        return len(result)

    def hash_password(self,password):
        return generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.data_user["password"],password)
