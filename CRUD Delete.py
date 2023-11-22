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
def conectar():
    return psycopg2.connect(**conexion_info)

def borrar_invitado(id):
    conexion = conectar()
    conexion.autocommit = True
    cursor = conexion.cursor()

    # Ejecutar la consulta de eliminación
    cursor.execute('DELETE FROM invitados', (id,))

    # Cerrar la conexión
    conexion.close()

borrar_invitado(int(input('Digite el id que desea eliminar: \n')))