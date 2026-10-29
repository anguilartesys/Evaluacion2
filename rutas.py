import requests

clave = "TU_TOKEN"


def buscar_lugar(lugar):
    r = requests.get("https://graphhopper.com/api/1/geocode",
                     params={"q": lugar, "limit": 1, "locale": "es", "key": clave})
    datos = r.json()
    if r.status_code != 200 or len(datos["hits"]) == 0:
        print("No se encontró el lugar:", lugar)
        return None
    punto = datos["hits"][0]["point"]
    return str(punto["lat"]) + "," + str(punto["lng"])


while True:
    print("\nMedios de transporte: car (auto), bike (bicicleta), foot (a pie)")
    print("Escriba s o salir para terminar")
    vehiculo = input("Medio de transporte: ").lower()
    if vehiculo in ["s", "salir"]:
        break
    if vehiculo not in ["car", "bike", "foot"]:
        print("Medio no válido, se usará car.")
        vehiculo = "car"

    origen = input("Origen: ")
    if origen.lower() in ["s", "salir"]:
        break
    destino = input("Destino: ")
    if destino.lower() in ["s", "salir"]:
        break

    punto_origen = buscar_lugar(origen)
    punto_destino = buscar_lugar(destino)
    if punto_origen is None or punto_destino is None:
        continue

    r = requests.get("https://graphhopper.com/api/1/route",
                     params={"point": [punto_origen, punto_destino], "profile": vehiculo,
                             "locale": "es", "key": clave})
    datos = r.json()
    print("Estado de la API de rutas:", r.status_code)
    if r.status_code != 200:
        print("Error:", datos["message"])
        continue

    ruta = datos["paths"][0]
    km = ruta["distance"] / 1000
    minutos = ruta["time"] / 1000 / 60
    print("\nDesde", origen, "hasta", destino, "en", vehiculo)
    print("Distancia: {:.2f} km / {:.2f} millas".format(km, km / 1.61))
    print("Duración: {:.2f} minutos".format(minutos))
    print("Indicaciones:")
    for paso in ruta["instructions"]:
        print("- {} ({:.2f} km)".format(paso["text"], paso["distance"] / 1000))

print("Programa terminado.")