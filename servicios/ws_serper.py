import http.client
import json

API_KEY = '722557a1524a77d20b492f7cc568c9f5e36d705c'

def buscar_en_serper(query):
    conn = http.client.HTTPSConnection("google.serper.dev")
    payload = json.dumps({
        "q": query
    })
    headers = {
        'X-API-KEY': API_KEY,
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/search", payload, headers)
    res = conn.getresponse()
    data = res.read()
    
    # Imprimir la respuesta completa para depuración
    print("Respuesta completa de Serper:")
    print(data.decode("utf-8"))