
import psycopg2
from psycopg2 import sql

conexion_info = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'admin',
    'port': '5432', 
}

# Conectarse a la nueva base de datos
nombre_nueva_bd = 'Plan_Descontrol'
conexion_info['database'] = nombre_nueva_bd
conexion = psycopg2.connect(**conexion_info)
conexion.autocommit = True
query = conexion.cursor()


# Crear una tabla llamada 'alumnos' en la nueva base de datos
query.execute('''
    CREATE TABLE IF NOT EXISTS invitados (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100),
        cedula VARCHAR(100),
        edad INTEGER)''')

query.execute('''
    CREATE TABLE IF NOT EXISTS licores (
        id SERIAL PRIMARY KEY,
        id_invitado INTEGER,
        licor_aportado VARCHAR(100))''')

# se recomienda siempre cerrar la conexion tras terminar un query para no exponer los datos y no consumir memoria ram
conexion.close()
print("se crean las tablas invitados, licores")