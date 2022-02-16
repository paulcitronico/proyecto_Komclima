import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "admin",
    "password": "administrador",
    "host": "localhost",
    "database": "temperatura"
}

try:
    con = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error en el usuario o contraseña")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Base de datos no existe")
    else:
        print(err)
else:
    con.close()