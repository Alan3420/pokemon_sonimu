from flask import Flask, render_template, jsonify, current_app
import json
from pathlib import Path

app = Flask(__name__, template_folder='templates')

with open("data/pokemon.json", encoding="utf-8") as f:
    app.config["data"] = json.load(f)
    
@app.route('/')
def Bienvenido():
    return render_template('index.html')

@app.route('/pokedex/')
def Pokedex():
    colorM = {
            "fire": "background: linear-gradient(to top, white 40%, red 100%);",
            "dragon": "purple",
            "grass": "background: linear-gradient(to top, white 40%, green 100%);",
            "normal": "gray",
            "fighting": "brown",
            "ground": "brown",
            "water": "background: linear-gradient(to top, white 40%, aqua 100%);",
            "dark":"pink",
            "flying":"aqua",
            "fairy": "salmon",
            "electric": "background: linear-gradient(to top, white 40%, yellow 100%);",
            "steel": "gray",
            "poison": "purple",
            "ice": "white"
        }
    
    return render_template('pokemons.html', pokemons = current_app.config["data"], colorM=colorM)

@app.route('/pokedex/<int:id>/')
def PokedexDetails(id):
    pokemons = current_app.config["data"]
    idPokemon = None
    for i in pokemons :
        if i['id'] == id:
            idPokemon = i
            break
    
    colorM = {
        "fire": "red",
        "dragon": "purple",
        "grass": "green",
        "normal": "gray",
        "fighting": "brown",
        "ground": "brown",
        "water": "blue",
        "dark":"pink",
        "flying":"aqua",
        "fairy": "salmon",
        "electric": "yellow",
        "steel": "gray",
        "poison": "purple",
        "ice": "white"
    }


    return render_template('pokemonsID.html', pokemon = idPokemon, colorM = colorM)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)