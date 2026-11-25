import requests

respuesta = requests.get("https://jsonplaceholder.typicode.com/todos/2")

datos = respuesta.json()

print("Usuario:", datos["userId"])
print("Tarea:", datos["title"])
print("Completada:", datos["completed"])