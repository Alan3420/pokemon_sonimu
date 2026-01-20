import app.repositories.pokemon_Repo as pokemon_repo
import app.clients.pokemon_clients as pokemonClient


def listar_pokemons():
    data = pokemonClient.get_pokemons()
    if not data or "results" not in data:
        return []

    # Iterar sobre cada Pokémon y adaptarlo
    pokemons = [adaptar_pokemon_list(p) for p in data["results"]]
    return pokemons

    # return pokemon_repo.obtener_Pokemons()


def obtener_pokemon_por_id(id):
    if id < 0 or id is None:
        return None

    data = pokemonClient.get_pokemon(id)

    if data is None:
        return None

    pokemon = adaptar_pokemon_detalle(data)
    return pokemon

    # return pokemon_repo.buscar_por_id(id)


def adaptar_pokemon_list(pokemon):
    url = pokemon.get("url")
    # Extraer id del URL: "https://pokeapi.co/api/v2/pokemon/1/" -> 1
    id = int(url.rstrip("/").split("/")[-1]) if url else None
    return {
        "id": id,
        "name": pokemon.get("name"),
        "url": url
    }


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


    return {
        "id": data.get("id"),
        "name": data.get("name"),
        "height": data.get("height"),
        "weight": data.get("weight"),
        "types": data.get("types"),
        "stats": listaStats
    }
