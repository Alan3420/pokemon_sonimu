import requests, time


class PokemonJsonClient:
    URL = "https://pokeapi.co/api/v2/pokemon"
    TTL = 1600

    def __init__(self):
        self._cache = {}

    def _get_cache(self, key):
        item = self._cache.get(key)

        if not item:
            return None

        if time.time() > item["tiempo"]:
            del self._cache[key]
            return None

        return item["value"]

    def _set_cache(self, key, value):
        self._cache[key] = {
            "value": value,
            "tiempo": time.time() + self.TTL
        }

    def get_pokemons(self):
        # falta poner una variable limit y un offset
        try:
            resp = requests.get(f"{self.URL}/?limit=5", timeout=5)
            resp.raise_for_status()
            return resp.json()
        except:
            return None

    def get_pokemon(self, id):
        cached = self._get_cache(id)
        if cached:
            return cached

        try:
            resp = requests.get(f"{self.URL}/{id}", timeout=5)
            resp.raise_for_status()
            data = resp.json()

            self._set_cache(id, data)
            return data
        except:
            return None

    def get_pokemonN(self, name):
        cached = self._get_cache(name)
        if cached:
            return cached

        try:
            resp = requests.get(f"{self.URL}/{name}", timeout=5)
            resp.raise_for_status()
            data = resp.json()

            self._set_cache(name, data)
            return data
        except:
            return None

    def get_movimientos(self, url):
        cached = self._get_cache(url)
        if cached:
            return cached

        try:
            resp = requests.get(url, timeout=4)
            resp.raise_for_status()
            data = resp.json()

            self._set_cache(url, data)
            return data
        except:
            return None
