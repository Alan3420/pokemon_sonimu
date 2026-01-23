import requests
import app.repositories.pokemon_Repo as pokemon_repo
from app.clients.pokemon_clients import PokemonJsonClient
from app.models.pokemon import Pokemon

pokemonClient = PokemonJsonClient()

def listar_pokemons():
    data = pokemonClient.get_pokemons()
    if not data or "results" not in data:
        return []
    
    listaPokemons = []
    for pokemon in data["results"]:
        url = pokemon["url"]
        
        id = int(url.rstrip("/").split("/")[-1])

        pokemonAdaptado = pokemonClient.get_pokemon(id)
        pokemonAdaptado = adaptar_pokemon_detalle(pokemonAdaptado)
        pokemons = Pokemon(**pokemonAdaptado)

        listaPokemons.append(pokemons)

    return listaPokemons


def obtener_pokemon_por_id(id):
    if id < 0 or id is None:
        return None

    data = pokemonClient.get_pokemon(id)

    if data is None:
        return None

    pokemon = adaptar_pokemon_detalle(data)
    return pokemon


def adaptar_pokemon_detalle(data):

    # ESTADISTICAS
    listaStats = []
    for stat in data["stats"]:
        name = stat["stat"]["name"]
        value = stat["base_stat"]

        listaStats.append({
            "name": name,
            "value": value
        })

    # TIPOS
    listaTipo = []
    for params in data["types"]:
        name = params["type"]["name"]

        listaTipo.append(name)

    # MOVIMIENTOS

    listaMovimientos = []
    for params in data["moves"][:10]:
    
        name = params["move"]["name"]
        url = params["move"]["url"]
        
        movimientos = pokemonClient.get_movimientos(url)

        
        
        accuracy = movimientos["accuracy"]
        power = movimientos["power"]
        type = movimientos["type"]["name"]

        listaMovimientos.append({
            "name": name,
            "accuracy": accuracy,
            "power": power,
            "type": type
        })

    # SPRITES
    sprites = {}
    for clave, valor in data["sprites"]["versions"]["generation-v"]["black-white"]["animated"].items():
        sprites.update({
            clave: valor
        })
    
    pokemonAdaptado = {
        "height": data["height"],
        "id":data["id"],
        "name": data["name"],
        "stats": listaStats,
        "sprites": sprites,
        "types": listaTipo,
        "weight": data["weight"],
        "moves": listaMovimientos

    }
    return pokemonAdaptado

