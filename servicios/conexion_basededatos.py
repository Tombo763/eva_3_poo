import mysql.connector

def create_connection():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='eva_3_poo'
        )
        if conexion.is_connected():
            print("Conexión a la base de datos exitosa.")
            return conexion
    except mysql.connector.Error as error:
        print(f"Error: {error}")
    return None
