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
conexion_info['database'] = 'Plan_Descontrol'
def conectar():
    return psycopg2.connect(**conexion_info)

def obtener_invitados():
    conexion = conectar()
    query = conexion.cursor()
    # Ejecutar la consulta de selección
    query.execute('SELECT * FROM invitados')
    invitados = query.fetchall()

    # Cerrar la conexión
    conexion.close()

    return invitados

invitados = obtener_invitados()
print("Invitados:", invitados)