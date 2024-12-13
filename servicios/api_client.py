import requests
from auxiliares.urls import url_base_jsonplaceholder

def fetch_users():
    response = requests.get(f"{url_base_jsonplaceholder}users")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener los datos: {response.status_code}")
        return None

def fetch_tasks():
    response = requests.get(f"{url_base_jsonplaceholder}todos")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener los datos: {response.status_code}")
        return None

