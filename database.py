import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PRODUCTS_FILENAME = os.path.join(BASE_DIR, 'productos.json')
USERS_FILENAME = os.path.join(BASE_DIR, 'usuarios.json')

def cargar_datos(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def guardar_datos(datos, filename):
    with open(filename, 'w') as file:
        json.dump(datos, file, indent=4)

def cargar_productos():
    return cargar_datos(PRODUCTS_FILENAME)

def guardar_productos(datos):
    guardar_datos(datos, PRODUCTS_FILENAME)

def cargar_usuarios():
    return cargar_datos(USERS_FILENAME)