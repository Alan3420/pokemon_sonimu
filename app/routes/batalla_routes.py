import random
from flask import Blueprint, render_template, request
import app.colors as color
from app.services import battle_service
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
    pokemonContrincante = battle_service.pokemonContrincante()

    # Pokemon elegido por el jugador
    pokemonJugadorUnico = battle_service.pokemonJugador(name)
    movimientos = battle_service.movimientosJugador(pokemonJugadorUnico)

    return render_template('batalla.html', pokemons = pokemons, pokemonContrincante = pokemonContrincante, pokemonJugadorUnico = pokemonJugadorUnico, colorM=color.colorM, movimientos = movimientos)
