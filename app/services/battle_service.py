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


class Batalla():

    def __init__(self, datos_pokemon_jugador, datos_pokemon_rival, hp_player, hp_rival):
        self.turno = 0
        self.log = []
        self.hp_player = hp_player
        self.hp_rival = hp_rival
        self.datos_pokemon_jugador = datos_pokemon_jugador
        self.datos_pokemon_rival = datos_pokemon_rival

    def siguienteTurno(self):
        self.turno += 1
        self.log.append(f"--- Turno {self.turno} ---")

    def dañoInflingido(self, golpea, recibe, movimiento):

        if self.datos_pokemon_jugador.stats["speed"] > self.datos_pokemon_rival.stats["speed"]:
            golpea = self.datos_pokemon_jugador
            recibe = self.datos_pokemon_rival
        else:
            recibe = self.datos_pokemon_jugador
            golpea = self.datos_pokemon_rival

        # daño simple = daño base * (ataque / defensa)
        dano = (golpea.stats["attack"]*movimiento["power"]
                )/recibe.stats["defense"]

    def formatMovimientoLog(self, movimiento, dano):
        mensaje = (
            f"{self.datos_pokemon_jugador.name} utilizó {movimiento}. "
            f"{self.datos_pokemon_rival.name} ha perdido {dano} puntos de salud. "
            f"PS restantes: {self.hp_rival - dano}."
        )
        self.log.append(mensaje)
        self.hp_rival -= dano

    def mostrarLog(self):
        for entrada in self.log:
            print(entrada)
