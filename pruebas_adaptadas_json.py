import requests


data= {
    "count": 1350,
    "next": "https://pokeapi.co/api/v2/pokemon?offset=5&limit=5",
    "previous": None,
    "results": [
        {
            "name": "bulbasaur",
            "url": "https://pokeapi.co/api/v2/pokemon/1/"
        },
        {
            "name": "ivysaur",
            "url": "https://pokeapi.co/api/v2/pokemon/2/"
        },
        {
            "name": "venusaur",
            "url": "https://pokeapi.co/api/v2/pokemon/3/"
        },
        {
            "name": "charmander",
            "url": "https://pokeapi.co/api/v2/pokemon/4/"
        },
        {
            "name": "charmeleon",
            "url": "https://pokeapi.co/api/v2/pokemon/5/"
        }
    ]
}

pokemons = []
for pokemon in data["results"]:
  url = pokemon["url"]
  print(url)

    # pokemonId = requests.get(url, timeout=5)
    # id = pokemonId.json()

    # pokemons.append(url)

