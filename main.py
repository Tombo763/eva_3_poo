from servicios.conexion_basededatos import create_connection
from modelos.usuarios import User
from modelos.tareas import Task
from servicios.api_client import fetch_users, fetch_tasks, create_user, update_user, delete_user, create_task, update_task, delete_task
from servicios.ws_serper import buscar_en_serper
from auxiliares.listas import usuarios

def insert_user(user, connection): #Insertar usuario.
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO Usuarios (id, name, username, email, phone, website)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (user.id, user.name, user.username, user.email, user.phone, user.website))
    connection.commit()

def insert_task(task, connection): #Insertar tarea.
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO Tareas (id, user_id, titulo, completada)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_query, (task.id, task.user_id, task.title, task.completed))
    connection.commit()

def verificar_usuarios(connection): #Consultar la tabla de usuarios.
    cursor = connection.cursor()
    select_query = "SELECT * FROM Usuarios"
    cursor.execute(select_query)
    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No hay usuarios en la base de datos.")

def verificar_tareas(connection): #Consultar la tabla de tareas.
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
        print("\n                                   ---> M E N Ú <---")
        print("""    
    | 1. Obtener y almacenar usuarios. | 2. Obtener y almacenar tareas. | 3. Crear un usuario. |
    |----------------------------------|--------------------------------|----------------------|
    | 4. Actualizar un usuario.        | 5. Eliminar un usuario.        | 6. Crear una tarea.  |
    |----------------------------------|--------------------------------|----------------------|
    | 7. Actualizar una tarea.         | 8. Eliminar una tarea.         | 9. Buscar en Serper. |
    |----------------------------------|--------------------------------|----------------------|
    | 10. Verificar usuarios.          | 11. Verificar tareas.          | 12. Salir.           |""")

        opcion = input("Selecciona una opción: ")

        try:
            opcion = int(opcion)
            if opcion == 1: #Obtener y almacenar usuarios.
                users_data = fetch_users()  # Aquí obtenemos los datos de los usuarios.
                if users_data:
                    users = [User(user['id'], user['name'], user['username'], user['email'], user['phone'], user['website']) for user in users_data]
                    for user in users:
                        insert_user(user, connection)
                        print(f'Usuario {user.name} insertado en la base de datos.')
                else:
                    print("No se pudieron obtener los datos de usuarios.")

            elif opcion == 2: #Obtener y almacenar tareas.
                tasks_data = fetch_tasks()  # Aquí obtenemos los datos de las tareas.
                if tasks_data:
                    tasks = [Task(task['id'], task['userId'], task['title'], task['completed']) for task in tasks_data]
                    for task in tasks:
                        insert_task(task, connection)
                        print(f'Tarea "{task.title}" insertada en la base de datos para el usuario {task.user_id}.')
                else:
                    print("No se pudieron obtener los datos de tareas.")
            
            elif opcion == 3: #Creamos el usuario.
                user_data = {
                    "name": input("Nombre: "),
                    "username": input("Nombre de usuario: "),
                    "email": input("Email: "),
                    "phone": input("Teléfono: "),
                    "website": input("Sitio web: ")
                }
                created_user = create_user(user_data)
                if created_user:
                    print("Usuario creado:", created_user)
                else:
                    print("No se pudo crear el usuario.")
            
            elif opcion == 4: #Actualizamos el usuario.
                user_id = int(input("ID del usuario a actualizar: "))
                user_data = {
                    "name": input("Nombre: "),
                    "username": input("Nombre de usuario: "),
                    "email": input("Email: "),
                    "phone": input("Teléfono: "),
                    "website": input("Sitio web: ")
                }
                updated_user = update_user(user_id, user_data)
                if updated_user:
                    print("Usuario actualizado:", updated_user)
                else:
                    print("No se pudo actualizar el usuario.")
            
            elif opcion == 5: #Eliminar un usuario.
                user_id = int(input("ID del usuario a eliminar: "))
                if delete_user(user_id):
                    print("Usuario eliminado.")
                else:
                    print("No se pudo eliminar el usuario.")
            
            elif opcion == 6: #Crear una tarea.
                task_data = {
                    "userId": int(input("ID del usuario: ")),
                    "title": input("Título: "),
                    "completed": input("Completada (true/false): ").lower() == "true"
                }
                created_task = create_task(task_data)
                if created_task:
                    print("Tarea creada:", created_task)
                else:
                    print("No se pudo crear la tarea.")
            
            elif opcion == 7: #Modificar tarea
                task_id = int(input("ID de la tarea a actualizar: "))
                task_data = {
                    "userId": int(input("ID del usuario: ")),
                    "title": input("Título: "),
                    "completed": input("Completada (true/false): ").lower() == "true"
                }
                updated_task = update_task(task_id, task_data)
                if updated_task:
                    print("Tarea actualizada:", updated_task)
                else:
                    print("No se pudo actualizar la tarea.")
            
            elif opcion == 8: #Eliminar una tarea.
                task_id = int(input("ID de la tarea a eliminar: "))
                if delete_task(task_id):
                    print("Tarea eliminada.")
                else:
                    print("No se pudo eliminar la tarea.")
            
            elif opcion == 9: #Buscar en serper.
                query = input("Ingresa la búsqueda que deseas realizar: ")
                resultados = buscar_en_serper(query)
                if resultados:
                    print("Resultados de la búsqueda:")
                    for item in resultados.get("results", []):
                        print(f"- {item.get('title')}: {item.get('link')}")
                else:
                    print("No se pudieron obtener resultados de Serper.")
            
            elif opcion == 10: #Mostrar usuarios guardados.
                print("Verificando usuarios en la base de datos...")
                verificar_usuarios(connection)
            
            elif opcion == 11: #Mostrar tareas guardadas.
                print("Verificando tareas en la base de datos...")
                verificar_tareas(connection)
            
            elif opcion == 12: #SALIR.
                print("Saliendo del programa.")
                break  # Fin del bucle.

            else: #Controla el rango numérico de las condicionales
                print("Opción no válida. Por favor, intenta de nuevo.")
        
        except ValueError: #Controla el error de valor.
            print("Por favor, ingresa un número válido.")
    
    connection.close()

# Ejecutar el programa principal
main()
