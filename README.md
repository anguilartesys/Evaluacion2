# Evaluacion2

Script en Python que calcula rutas entre dos lugares usando la API de GraphHopper Directions. Es una versión mejorada del prototipo de geolocalización para la Biblioteca Nacional.

## Cambios respecto al script original

- Mensajes al usuario en español.
- Distancias y tiempos con dos decimales como máximo.
- Se puede salir escribiendo `s` o `salir`.
- Indicaciones del viaje en español.

## Requisitos

- Python 3
- Librería requests (`pip3 install requests`)
- Un token de GraphHopper

## Cómo ejecutarlo

1. Abrir `rutas.py` y reemplazar `TU_TOKEN` por el token de GraphHopper.
2. Ejecutar `python3 rutas.py`.
3. Ingresar el medio de transporte (car, bike o foot), el origen y el destino.
4. Escribir `s` o `salir` para terminar.

## Autores

Antulio, Ignacio, Rodrigo y Manolo. CUY6142, Duoc UC.
