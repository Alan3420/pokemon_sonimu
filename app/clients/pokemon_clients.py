import requests
def get_pokemons():
    url = "https://pokeapi.co/api/v2/pokemon?limit=20"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        return resp.json()
    except:
        return None

def get_pokemon(id):
    url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        return resp.json()
    except:
        return None