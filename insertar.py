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
        #cursor.execute("INSERT into usuarios (nombre,apellido,edad,correo) values () ")
        sentencia = "INSERT into usuarios (nombre,apellido,edad,correo) values ('{0}','{1}','{2}','{3}')".format(nombre,apellido,edad,correo)
        cursor.execute(sentencia)
        conexion.commit() #Confirmar la accion que estamos ejecutando
        print("Registro insertado con exito!")
except Error as ex:
    print("Error durante la ejecusión : ", ex)

finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexion ha finalizado")