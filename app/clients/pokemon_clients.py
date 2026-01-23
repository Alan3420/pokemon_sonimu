import requests
class PokemonJsonClient:
    URL = "https://pokeapi.co/api/v2/pokemon"

    def __init__(self):
        self._cache = {}

    def get_pokemons(self):
        try:
            resp = requests.get(f"self.URL?limit=5", timeout=5)
            resp.raise_for_status()
            return resp.json()
        except:
            return None

    def get_pokemon(self, id):
        if id in self._cache:
            return self._cache[id]        
        try:
            resp = requests.get(f"self.URL/{id}", timeout=5)
            resp.raise_for_status()
            data = resp.json()

            self._cache[id] = data
            return data
        except:
            return None
        
    def get_movimientos(self, url):
        if id in self._cache:
            return self._cache[id]
        
        try:   
            resp = requests.get(url, timeout=4)
            resp.raise_for_status()
            data = resp.json()
        
            self._cache[id] = data
            return data
        except:
            return None