from flask import request
import app.repositories.pokemon_Repo as pokemon_repo
from app.clients.pokemon_clients import PokemonJsonClient
from app.models.pokemon import Pokemon

pokemonClient = PokemonJsonClient()

def listar_pokemons(limit=5, page=1):
    data = pokemonClient.get_pokemons(limit, page)
    if not data or "results" not in data:
        return []
    
    listaPokemons = []
    for pokemon in data["results"]:
        url = pokemon["url"]
        
        id = int(url.rstrip("/").split("/")[-1])

        pokemonAdaptado = pokemonClient.get_pokemon(id)

        if pokemonAdaptado is None:
            print(f"Error: No se pudo obtener el Pokémon con ID {id}")
            continue  # Saltar este Pokémon y continuar con el siguiente
        
        pokemonAdaptado = adaptar_pokemon_detalle(pokemonAdaptado)
        pokemons = Pokemon(**pokemonAdaptado)

        listaPokemons.append(pokemons)

    return listaPokemons, data["count"]


def obtener_pokemon_por_id(id):
    if id < 0 or id is None:
        return None

    data = pokemonClient.get_pokemon(id)

    if data is None:
        return None

    pokemon = adaptar_pokemon_detalle(data)
    pokemon = Pokemon(**pokemon)
    return pokemon

def obtener_pokemon_por_name(name):
    data = pokemonClient.get_pokemonN(name)

    if data is None:
        return None

    pokemon = adaptar_pokemon_detalle(data)
    pokemon = Pokemon(**pokemon)
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
    for params in data["moves"]:
        if len(listaMovimientos) >= 10:
            break

        url = params["move"]["url"]

        movimiento = pokemonClient.get_movimientos(url)

        
        if movimiento and movimiento["power"] is not None:
            name = movimiento["name"]
            accuracy = movimiento["accuracy"]
            power = movimiento["power"]
            type = movimiento["type"]["name"]

            listaMovimientos.append({
                "name": name,
                "accuracy": accuracy,
                "power": power,
                "type": type
            })


    # SPRITES
    sprites = {}
    animated = data["sprites"]["versions"]["generation-v"]["black-white"]["animated"]
    

    for clave, valor in animated.items():
        if valor is not None:
            sprites[clave] = valor
        else:
            sprites[clave] = data["sprites"].get(clave)

    
    pokemonAdaptado = {
        "height": data["height"],
        "id":data["id"],
        "name": data["species"]["name"],
        "stats": listaStats,
        "sprites": sprites,
        "types": listaTipo,
        "weight": data["weight"],
        "moves": listaMovimientos

    }
    return pokemonAdaptado

def paginacionPokemon():
    pagina = request.args.get('page', 1, type=int)
    limite = request.args.get('limit', 5, type=int)
    

    todos_pokemons, total = listar_pokemons(limit=limite, page=pagina)

    pokemons_pagina = todos_pokemons


    total_pages = (total + limite - 1) // limite
    prev_page = None
    next_page = None

    if pagina > 1:
        prev_page = pagina - 1
    else:
        prev_page = None
    
    if pagina < total_pages: 
        next_page = pagina + 1 
    else:
        next_page = None   

    pagination = {
        'page': pagina,
        'total': total,
        'total_pages': total_pages,
        'prev_page': prev_page,
        'next_page': next_page,
        'pokemon_pagina': pokemons_pagina
    }

    return pagination