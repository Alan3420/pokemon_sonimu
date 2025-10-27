from flask import Flask, render_template, jsonify, current_app, request
import json,random
from pathlib import Path
import app.services.pokemon_services as pokemon_services
import colors as color

app = Flask(__name__, template_folder='templates')

with open("data/pokemon.json", encoding="utf-8") as f:
    app.config["data"] = json.load(f)
    
@app.route('/')
def Bienvenido():

    if request.method == "GET":
        render_template('index.html')

    if request.method == "POST":
        user = request.form.get("nombre")

    return render_template('index.html')


@app.route('/pokedex/')
def Pokedex():
    
    
    return render_template('pokemons.html', pokemons = current_app.config["data"], colorM=color.colorT)



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

    
    return render_template('pickPokemon.html', pokemons = current_app.config["data"], colorM=color.colorT ,nombreUser = nombre)

@app.route('/batallasPokemon/<name>/', methods=["POST", "GET"])
def BatallaP(name):

    nombre = request.args.get("pokemon", "")
    nombre = nombre.strip()
    pokemons = current_app.config["data"]

    # Pokemons aleatorios de contrincante
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
        movimientos = random.sample(pokemonJugadorUnico["moves"], 4)

    

    return render_template('batalla.html', pokemons = pokemons, pokemonContrincante = pokemonContrincante, pokemonJugadorUnico = pokemonJugadorUnico, colorM=color.colorM, movimientos = movimientos)

@app.route('/pokedex/<int:id>/')
def PokedexDetails(id):

    idPokemon = pokemon_services.obtener_pokemon_por_id(id)


    return render_template('pokemonsID.html', pokemon = idPokemon, colorM = color.colorM)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)