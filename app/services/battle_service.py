import random

from flask import render_template, request
import app.repositories.pokemon_Repo as pokemon_repo
from app.services import pokemon_services


def pokemonContrincante():

    pokemons = pokemon_services.listar_pokemons()

    return random.choice(pokemons)


def movimientosContrincante(pokemonContrincanteUnico):

    # Si el jugador a seleccionado un pokemon se cargaran su sets de movimientos de forma aleatoria
    if pokemonContrincanteUnico != None:
        movimientos = random.sample(pokemonContrincanteUnico.moves, 4)

    return movimientos


def pokemonJugador(name):

    nombre = request.args.get("pokemon", "")
    nombre = nombre.strip()

    pokemons = pokemon_services.listar_pokemons()
    # Pokemon elegido por el jugador
    pokemonJugadorUnico = None

    for pokemon in pokemons:
        # verificamos que el nombre que nos envian desde el formulario esta en la lista de pokemones disponibles
        if pokemon.name.lower() == nombre.lower() or pokemon.name.lower() == name:
            pokemonJugadorUnico = pokemon
            break

    if pokemonJugadorUnico == None:
        mensaje = "El pokemon "+nombre+" no se encuentra en la lista de la Pokedex."
        return render_template("error404.html", mensaje=mensaje), 404

    return pokemonJugadorUnico


def movimientosJugador(pokemonJugadorUnico):

    # Si el jugador a seleccionado un pokemon se cargaran su sets de movimientos de forma aleatoria
    if pokemonJugadorUnico != None:
        movimientos = random.sample(pokemonJugadorUnico.moves, 4)

    return movimientos

# class Batlla():
#     turno = 0
#     datos_pokemon_jugador = {
#         pokemonJugador(),
#         movimientosJugador()
#     }

#     datos_pokemon_rival = {
#         pokemonContrincante(),
#         movimientosContrincante()
#     }
