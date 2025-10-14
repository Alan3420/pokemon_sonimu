from flask import Flask, render_template, jsonify, current_app, request
import json
from pathlib import Path

app = Flask(__name__, template_folder='templates')

with open("data/pokemon.json", encoding="utf-8") as f:
    app.config["data"] = json.load(f)
    
@app.route('/')
def Bienvenido():

    if request.method == "GET":
        render_template('index.html')

    if request.method == "POST":
        user = request.form.get("nombre")
        password = request.form.get("password")

    return render_template('index.html')
    # , f"Hola, {user}, tu password es {password}"

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

@app.route('/pokedexSeleccion/')
def PokedexS():
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
    
    return render_template('pickPokemon.html', pokemons = current_app.config["data"], colorM=colorM)

@app.route('/pokedex/<int:id>/', methods=["POST", "GET"])
def PokedexDetails(id):
    
    # validar el nombre del entrenador
    error = None
    nombre = request.form.get("nombre", "").strip()

 
    

    # if request.method == "GET":

    
    


    pokemons = current_app.config["data"]
    idPokemon = None
    for i in pokemons :
        if i['id'] == id:
            idPokemon = i
            break
    
    colorM = {
        "fire": "border: 4px groove rgba(255, 0, 0)",
        "dragon": "border: 4px groove rgba(123,104,238)",
        "grass": "border: 4px groove rgba(0, 255, 0)",
        "normal": "border: 4px groove rgba(200, 200, 200)",
        "fighting": "border: 4px groove rgba(255, 165, 0)",
        "ground": "border: 4px groove rgb(203, 91, 43)",
        "water": "border: 4px groove rgba(23, 140, 184)",
        "dark":"border: 4px groove rgba(30, 30, 30)",
        "flying":"border: 4px groove rgba(135, 206, 235)",
        "fairy": "border: 4px groove rgba(255, 192, 203)",
        "electric": "border: 4px groove rgba(255, 255, 0)",
        "steel": "border: 4px groove rgb(37, 150, 190)",
        "poison": "border: 4px groove rgba(128, 0, 128)",
        "ice": "border: 4px groove rgba(173, 216, 230)"
    }


    return render_template('pokemonsID.html', pokemon = idPokemon, colorM = colorM)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)