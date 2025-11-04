import random
from flask import Blueprint, render_template, request
import app.colors as color
from app.services import pokemon_services

batalla_pb = Blueprint('batalla_route',__name__,template_folder='templates')

@batalla_pb.route('/pokedexSeleccion/', methods=["POST", "GET"])
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

    
    return render_template('pickPokemon.html', pokemons = pokemon_services.listar_pokemons(), colorM=color.colorT ,nombreUser = nombre)

@batalla_pb.route('/batallasPokemon/<name>/', methods=["POST", "GET"])
def BatallaP(name):

    nombre = request.args.get("pokemon", "")
    nombre = nombre.strip()
    pokemons = pokemon_services.listar_pokemons()

    # Pokemons aleatorios de contrincante
    pokemonContrincante = random.choice(pokemons)

    # Pokemon elegido por el jugador
    pokemonJugadorUnico = None

    for pokemon in pokemons:
        # verificamos que el nombre que nos envian desde el formulario esta en la lista de pokemones disponibles
        if pokemon.name.lower() == nombre.lower()  or pokemon.name.lower() == name:
            pokemonJugadorUnico = pokemon
            break
    
    # Si el jugador a seleccionado un pokemon se cargaran su sets de movimientos de forma aleatoria
    if pokemonJugadorUnico != None:
        movimientos = random.sample(pokemonJugadorUnico.moves, 4)
    
    elif pokemonJugadorUnico == None:
        mensaje = "El pokemon "+nombre+" no se encuentra en la lista de la Pokedex."
        return render_template("error404.html", mensaje = mensaje), 404

    # En caso contrario se cargaran los movimientos del pokemon que a sido elegido para el jugador tambien de forma aleatoria
    else:
        movimientos = random.sample(pokemonJugadorUnico.moves, 4)

    

    return render_template('batalla.html', pokemons = pokemons, pokemonContrincante = pokemonContrincante, pokemonJugadorUnico = pokemonJugadorUnico, colorM=color.colorM, movimientos = movimientos)
