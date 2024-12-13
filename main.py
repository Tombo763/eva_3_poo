from servicios.conexion_basededatos import create_connection
from modelos.usuarios import User
from modelos.tareas import Task
from servicios.api_client import fetch_users, fetch_tasks
from servicios.ws_serper import buscar_en_serper
from auxiliares.listas import usuarios

def insert_user(user, connection):
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO Usuarios (id, name, username, email, phone, website)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (user.id, user.name, user.username, user.email, user.phone, user.website))
    connection.commit()

def insert_task(task, connection):
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO Tareas (id, user_id, titulo, completada)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_query, (task.id, task.user_id, task.title, task.completed))
    connection.commit()

def verificar_usuarios(connection):
    cursor = connection.cursor()
    select_query = "SELECT * FROM Usuarios"
    cursor.execute(select_query)
    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No hay usuarios en la base de datos.")

def verificar_tareas(connection):
    cursor = connection.cursor()
    select_query = "SELECT * FROM Tareas"
    cursor.execute(select_query)
    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No hay tareas en la base de datos.")

def main():
    connection = create_connection()
    if not connection:
        print("No se pudo conectar a la base de datos. Saliendo del programa.")
        return
    
    while True:
        print("\n--- MENÚ ---")
        print("1. Obtener y almacenar usuarios.")
        print("2. Obtener y almacenar tareas.")
        print("3. Buscar en Serper.")
        print("4. Verificar usuarios.")
        print("5. Verificar tareas.")
        print("6. Salir.")

        opcion = input("Selecciona una opción: ")

        try:
            opcion = int(opcion)
            if opcion == 1:
                users_data = fetch_users()  # Aquí obtenemos los datos de los usuarios.
                if users_data:
                    users = [User(user['id'], user['name'], user['username'], user['email'], user['phone'], user['website']) for user in users_data]
                    for user in users:
                        insert_user(user, connection)
                        print(f'Usuario {user.name} insertado en la base de datos.')
                else:
                    print("No se pudieron obtener los datos de usuarios.")

            elif opcion == 2:
                tasks_data = fetch_tasks()  # Aquí obtenemos los datos de las tareas.
                if tasks_data:
                    tasks = [Task(task['id'], task['userId'], task['title'], task['completed']) for task in tasks_data]
                    for task in tasks:
                        insert_task(task, connection)
                        print(f'Tarea "{task.title}" insertada en la base de datos para el usuario {task.user_id}.')
                else:
                    print("No se pudieron obtener los datos de tareas.")
            
            elif opcion == 3:
                query = input("Ingresa la búsqueda que deseas realizar: ")
                resultados = buscar_en_serper(query)
                if resultados:
                    print("Resultados de la búsqueda:")
                    for item in resultados.get("results", []):
                        print(f"- {item.get('title')}: {item.get('link')}")
                else:
                    print("No se pudieron obtener resultados de Serper.")
            
            elif opcion == 4:
                print("Verificando usuarios en la base de datos...")
                verificar_usuarios(connection)
            
            elif opcion == 5:
                print("Verificando tareas en la base de datos...")
                verificar_tareas(connection)
            
            elif opcion == 6:
                print("Saliendo del programa.")
                break  # Fin del bucle.

            else:
                print("Opción no válida. Por favor, intenta de nuevo.")
        
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    connection.close()

# Ejecutar el programa principal
main()
