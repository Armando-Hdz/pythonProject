import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = '12345678',
        db = 'crudbasicpyt'
    )
    if conexion.is_connected():
        print("Conexion Exitosa! ")
        cursor = conexion.cursor()
        id = input("Ingresa el ID del usuario que deseas eliminar: ")

        sentencia = "DELETE from usuarios WHERE id = '{0}'".format(id)
        cursor.execute(sentencia)
        conexion.commit() #Confirmar la accion que estamos ejecutando
        print("Registro eliminado con exito!")
except Error as ex:
    print("Error durante la ejecusión : ", ex)

finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexion ha finalizado")