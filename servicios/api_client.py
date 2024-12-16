import requests
from auxiliares.urls import url_base_jsonplaceholder


def fetch_users(): # Obtenemos los usuarios.
    response = requests.get(f"{url_base_jsonplaceholder}users")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener los datos: {response.status_code}")
        return None


def fetch_tasks(): # Obtenemos las tareas.
    response = requests.get(f"{url_base_jsonplaceholder}todos")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener los datos: {response.status_code}")
        return None


def create_user(user_data): #Utilizamos el método post para crear nuevos usuarios.
    response = requests.post(f"{url_base_jsonplaceholder}users", json=user_data)
    if response.status_code == 201:
        return response.json()
    else:
        print(f"Error al crear el usuario: {response.status_code}")
        return None

def update_user(user_id, user_data): #Utilizamos el método put para modificar un usuario.
    response = requests.put(f"{url_base_jsonplaceholder}users/{user_id}", json=user_data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al actualizar el usuario: {response.status_code}")
        return None

def delete_user(user_id): #Utilizamos el método delete para eliminar un usuario.
    response = requests.delete(f"{url_base_jsonplaceholder}users/{user_id}")
    if response.status_code == 200:
        return True
    else:
        print(f"Error al eliminar el usuario: {response.status_code}")
        return False


def create_task(task_data): # Utilizamos post para crear una nueva tarea.
    response = requests.post(f"{url_base_jsonplaceholder}todos", json=task_data)
    if response.status_code == 201:
        return response.json()
    else:
        print(f"Error al crear la tarea: {response.status_code}")
        return None

def update_task(task_id, task_data): #Con el put modificamos o actualizamos una tarea.
    response = requests.put(f"{url_base_jsonplaceholder}todos/{task_id}", json=task_data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al actualizar la tarea: {response.status_code}")
        return None


def delete_task(task_id): # Se utiliza delete para eliminar una tarea.
    response = requests.delete(f"{url_base_jsonplaceholder}todos/{task_id}")
    if response.status_code == 200:
        return True
    else:
        print(f"Error al eliminar la tarea: {response.status_code}")
        return False
