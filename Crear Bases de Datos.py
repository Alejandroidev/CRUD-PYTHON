
import psycopg2
from psycopg2 import sql

# Establecer la conexión a la instancia de la base de datos 

conexion_info = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'admin',
    'port': '5432', 
}

# Conectar a la base de datos
conexion = psycopg2.connect(**conexion_info)
conexion.autocommit = True

# Crear un cursor para ejecutar consultas SQL 
query = conexion.cursor()

# Crear una base de datos 

# genera el query
query.execute(sql.SQL('CREATE DATABASE {}').format(sql.Identifier('Plan_Descontrol')))

# se recomienda siempre cerrar la conexion tras terminar un query para no exponer los datos y no consumir memoria ram
conexion.close()

print("Se crea BD Plan_Tranqui")