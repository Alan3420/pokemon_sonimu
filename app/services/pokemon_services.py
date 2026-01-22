import requests
import app.repositories.pokemon_Repo as pokemon_repo
import app.clients.pokemon_clients as pokemonClient


def listar_pokemons():
    data = pokemonClient.get_pokemons()
    if not data or "results" not in data:
        return []
    
    pokemons = []
    for pokemon in data:
        url = pokemon["results"]["url"]
        pokemonId = requests.get(url, timeout=5)
        id = pokemonId.json()
        
        pokemonAdaptado = pokemonClient.get_pokemon(id["id"])
        pokemonAdaptado = adaptar_pokemon_detalle(id["id"])

        pokemons.append(pokemonAdaptado)
    
    return pokemons


def obtener_pokemon_por_id(id):
    if id < 0 or id is None:
        return None

    data = pokemonClient.get_pokemon(id)

    if data is None:
        return None

    pokemon = adaptar_pokemon_detalle(data)
    return pokemon

def adaptar_pokemon_detalle(data):
    name = None
    value = None
    listaStats = []
    for stat in data["stats"]:
            
        name = stat["stat"]["name"]
        value = stat["base_stat"]

        listaStats.append({
            "name": name,
            "value": value
        })

    listaTipo = []
    for params in data["types"]:
        
        
        name = params["type"]["name"]

        listaTipo.append(name)

    listaMovimientos = []

    for params in data["moves"][:10]:
    
        name = params["move"]["name"]
        url = params["move"]["url"]
        

        movimientos = requests.get(url, timeout=4)
        mov_acc = movimientos.json()
        accuracy = mov_acc["accuracy"]
        power = mov_acc["power"]
        type = mov_acc["type"]["name"]

        listaMovimientos.append({
            "name": name,
            "accuracy": accuracy,
            "power": power,
            "type": type


        })

    # acceso a los sprites: sprites > versions > generation-v > black-white > animated 
    sprites = []
    for clave, valor in data["sprites"]["versions"]["generation-v"]["black-white"]["animated"].items():
        sprites.append({
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
