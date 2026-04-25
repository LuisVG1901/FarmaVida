import mysql.connector
import os

def conectar():
    conexion = mysql.connector.connect(
        host=os.environ.get("mysql.railway.internal"),
        user=os.environ.get("root"),
        password=os.environ.get("uiFcrNEPnoOXCrSLPDoHSjYbSpEhxdiT"),
        database=os.environ.get("railway"),
        port=int(os.environ.get("MYSQLPORT", 3306))
    )
    return conexion