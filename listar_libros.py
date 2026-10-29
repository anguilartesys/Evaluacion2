import requests

url = "http://library.demo.local/api/v1"
pagina = 0
total = 0

while True:
    r = requests.get(url + "/books", params={"includeISBN": "true", "page": pagina})
    libros = r.json()
    if len(libros) == 0:
        break
    print("--- Página", pagina, "- estado", r.status_code)
    for libro in libros:
        print(libro["id"], libro["isbn"], libro["author"], "-", libro["title"])
    total += len(libros)
    if len(libros) < 10:
        break
    pagina += 1

print("Total de libros:", total)