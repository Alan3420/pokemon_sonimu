from flask import Flask, render_template, jsonify, current_app, request
import json,random
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

@app.route('/pokedexSeleccion/', methods=["POST", "GET"])
def PokedexS():

    # validar el nombre del entrenador
    nombre = request.args.get("nombre", "")
    nombre = nombre.strip()

    if len(nombre) > 15:
        mensaje = "Advertencia: el nombre debe tener como maximo 15 caracteres"
        return render_template("index.html", mensaje = mensaje)
    elif len(nombre) < 3:
        mensaje = "Advertencia: el nombre debe tener como minimo 3 caracteres"
        return render_template("index.html", mensaje = mensaje)

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
    
    return render_template('pickPokemon.html', pokemons = current_app.config["data"], colorM=colorM ,nombreUser = nombre)

@app.route('/batallasPokemon/<name>/', methods=["POST", "GET"])
def BatallaP(name):

    nombre = request.args.get("pokemon", "")
    nombre = nombre.strip()
    pokemons = current_app.config["data"]

    # Pokemons aleatorios de contrincante y si el jugador no elige ninguno toma otro de forma aleatorio
    pokemonContrincante = random.choice(pokemons)
    pokemonJugador = random.choice(pokemons)

    while pokemonJugador==pokemonContrincante:
        pokemonContrincante = random.choice(pokemons)


    # Pokemon elegido por el jugador
    pokemonJugadorUnico = None

    for pokemon in pokemons:
        # verificamos que el nombre que nos envian desde el formulario esta en la lista de pokemones disponibles
        if pokemon["name"] == nombre.lower()  or pokemon["name"] == name:
            pokemonJugadorUnico = pokemon
            break
    
    # Si el jugador a seleccionado un pokemon se cargaran su sets de movimientos de forma aleatoria
    if pokemonJugadorUnico != None:
        movimientos = random.sample(pokemonJugadorUnico["moves"], 4)
    
    elif pokemonJugadorUnico == None:
        mensaje = "El pokemon "+nombre+" no se encuentra en la lista de la Pokedex."
        return render_template("error404.html", mensaje = mensaje), 404

    # En caso contrario se cargaran los movimientos del pokemon que a sido elegido para el jugador tambien de forma aleatoria
    else:
        movimientos = random.sample(pokemonJugador["moves"], 4)

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

    return render_template('batalla.html', pokemons = pokemons, pokemonContrincante = pokemonContrincante, pokemonJugador = pokemonJugador , pokemonJugadorUnico = pokemonJugadorUnico, colorM=colorM, movimientos = movimientos)

@app.route('/pokedex/<int:id>/')
def PokedexDetails(id):

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