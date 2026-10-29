import requests
import random

url = "http://library.demo.local/api/v1"

r = requests.post(url + "/loginViaBasic", auth=("cisco", "Cisco123!"))
headers = {"X-API-KEY": r.json()["token"]}

nombres = ["Juan", "María", "Pedro", "Camila", "Diego", "Valentina", "Jorge", "Fernanda"]
apellidos = ["González", "Muñoz", "Rojas", "Díaz", "Pérez", "Soto", "Contreras", "Silva"]
temas = ["Redes", "Python", "Seguridad", "Linux", "Cloud", "Automatización", "Bases de Datos", "APIs"]
estilos = ["para Principiantes", "Avanzado", "en la Práctica", "Paso a Paso", "Esencial", "Moderno"]

for i in range(8, 58):
    libro = {
        "id": i,
        "title": random.choice(temas) + " " + random.choice(estilos),
        "author": random.choice(nombres) + " " + random.choice(apellidos),
        "isbn": str(random.randint(1000000000000, 9999999999999)),
    }
    r = requests.post(url + "/books", headers=headers, json=libro)
    print(r.status_code, libro["id"], libro["title"], "-", libro["author"])

r = requests.get(url + "/books", params={"includeISBN": "true"})
libros = r.json()
for libro in libros:
    print(libro["id"], libro["isbn"], libro["author"], "-", libro["title"])
print("Total de libros:", len(libros))