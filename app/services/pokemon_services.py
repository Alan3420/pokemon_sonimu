import repositories.pokemon_Repo as pokemon_repo


def listar_pokemons():
    return pokemon_repo.obtener_Pokemons()

def obtener_pokemon_por_id(id):

    if id < 0 or id is None:
        return None
    
    return pokemon_repo.buscar_por_id(id)