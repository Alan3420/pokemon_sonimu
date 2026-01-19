import requests

url = "https://pokeapi.co/api/v2/pokemon?limit=20"
response = requests.get(url)