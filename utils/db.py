import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "admin",
    "password": "administrador",
    "host": "localhost",
    "database": "temperatura"
}

con = mysql.connector.connect(**config)