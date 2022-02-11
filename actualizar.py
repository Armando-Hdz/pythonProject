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
        nombre = input("Ingrese el nombre del usuario: ")
        apellido = input("Ingrese el apellido del usuario: ")
        edad = input("Ingrese la edad del usuario: ")
        correo = input("Ingrese el correo del usuario: ")
        id = input("Ingresa el ID del usuario que deseas modificar: ")

        sentencia = """UPDATE usuarios SET nombre='{0}',apellido='{1}',edad='{2}',correo='{3}'
                    where id = '{4}'""".format(nombre,apellido,edad,correo,id)
        cursor.execute(sentencia)
        conexion.commit() #Confirmar la accion que estamos ejecutando
        print("Registro actualizado con exito!")
except Error as ex:
    print("Error durante la ejecusión : ", ex)

finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexion ha finalizado")