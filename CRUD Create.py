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
conexion = psycopg2.connect(**conexion_info)
conexion.autocommit = True
query = conexion.cursor()

# Función para insertar un nuevo invitado
def insertar_invitado(nombre, cedula, edad):
    query.execute('INSERT INTO invitados (nombre, cedula, edad) VALUES (%s , %s, %s)', (nombre, cedula, edad))
    conexion.commit()

#nombre_nuevo_invitado = input('Ingrese nombre:  \n')
#cedula_nuevo_invitado = input('Ingrese cedula:  \n')
#edad_nuevo_invitado = int(input('edad:  \n'))

#insertar_invitado(nombre_nuevo_invitado, cedula_nuevo_invitado, edad_nuevo_invitado)
insertar_invitado('sergio', 'CC: 101666500', 23)
insertar_invitado('sebastian', 'CC: 1015992500', 21)
insertar_invitado('jonathan', 'CC: 10150032500', 24)
insertar_invitado('harold', 'CC: 10167899843', 25)

# se recomienda siempre cerrar la conexion tras terminar un query para no exponer los datos y no consumir memoria ram
conexion.close()
print("se agrega invitado \n")