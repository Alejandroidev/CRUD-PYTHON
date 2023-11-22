
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

def actualizar_invitado(id, nombre, cedula, edad):
    conexion = conectar()
    conexion.autocommit = True
    query = conexion.cursor()
    # Ejecutar la consulta de actualización
    query.execute('UPDATE invitados SET nombre=%s, cedula=%s, edad=%s WHERE id=%s', (nombre, cedula, edad, id))
    # Cerrar la conexión
    conexion.close()

id = int(input('Id invitado:  \n'))
nombre_nuevo_invitado = input('Ingrese nombre:  \n')
cedula_nuevo_invitado = input('Ingrese cedula:  \n')
edad_nuevo_invitado = int(input('edad:  \n'))

actualizar_invitado(id, nombre_nuevo_invitado, cedula_nuevo_invitado, edad_nuevo_invitado)