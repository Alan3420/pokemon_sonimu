import json
from pathlib import Path
import sqlite3

from app.models.pokemon import Pokemon


DATA_PATH = Path(__file__).parent.parent.parent / "data" / "pokemon.json"

with open(DATA_PATH , encoding="utf-8") as fichero_data:
     _POKEMONS = json.load(fichero_data)


def obtener_Pokemons():

    pokemons = []

    for p in _POKEMONS:

        # **p toma todos los elementos de un diccionario para un objeto,
        # ahorrando ir elemento a elemento de un mismo objeto ejemplo
        # Pokemon(id = p['id'], name = p['name'] etc)

        pokemon = Pokemon(**p)
        pokemons.append(pokemon)

    return pokemons


def buscar_por_id(id):
    pokemons = obtener_Pokemons()

    for p in pokemons:
        if p.id == id:
            pokemon = p
            break

    return pokemon


def get_connection():
    conn = sqlite3.connect("data/pokemons.db")
    conn.row_factory = sqlite3.Row
    return conn
