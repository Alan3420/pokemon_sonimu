import requests

url = "https://pokeapi.co/api/v2/pokemon?limit=20"

# Ejemplo parametros
# params = {"q": "laptop"}
# response = requests.get(url, params=params)

response = requests.get(url)

if response.status_code == 200:
    data = response.json()