import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host = 'tecnicaencolectores.com.mx',
        port = 3306,
        user = 'tecnicae',
        password = 'empresa21Tecs@',
        db = 'tecsaoffice'
    )
    if conexion.is_connected():
        print("Conexion Exitosa! ")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM module")
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)
except Error as ex:
    print("Error durante la ejecusión : ", ex)

finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexion ha finalizado")