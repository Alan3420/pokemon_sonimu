import requests, json

class PokemonJsonClient:
    URL = "https://pokeapi.co/api/v2/pokemon"

    def __init__(self):
        self._cache = {}

    def get_pokemons(self):
        try:
            resp = requests.get(f"{self.URL}/?limit=5", timeout=5)
            resp.raise_for_status()
            data = resp.json()
            return data
        except:
            return None

    def get_pokemon(self, id):
        if id in self._cache:
            return self._cache[id]        
        try:
            resp = requests.get(f"{self.URL}/{id}", timeout=5)
            resp.raise_for_status()
            data = resp.json()

            self._cache[id] = data
            return data
        except:
            return None
        
    def get_pokemonN(self, name):
        if name in self._cache:
            return self._cache[name]        
        try:
            resp = requests.get(f"{self.URL}/{name}", timeout=5)
            resp.raise_for_status()
            data = resp.json()

            self._cache[name] = data
            return data
        except:
            return None
        
    def get_movimientos(self, url):
        if url in self._cache:
            return self._cache[url]
        try:   
            resp = requests.get(url, timeout=4)
            resp.raise_for_status()
            data = resp.json()
        
            self._cache[url] = data
            return data
        except:
            return None