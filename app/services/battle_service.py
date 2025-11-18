import random

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

    
    nombre = name.strip().lower()

    pokemons = pokemon_services.listar_pokemons()

    for pokemon in pokemons:
        # verificamos que el nombre que nos envian desde el formulario esta en la lista de pokemones disponibles
        if pokemon.name.lower() == nombre:
            pokemonJugadorUnico = pokemon
            return pokemonJugadorUnico

    return None


def movimientosJugador(pokemonJugadorUnico):

    # Si el jugador a seleccionado un pokemon se cargaran su sets de movimientos de forma aleatoria
    if pokemonJugadorUnico != None:
        movimientos = random.sample(pokemonJugadorUnico.moves, 4)

    return movimientos
