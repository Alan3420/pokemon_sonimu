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

def getStat(self, poke, nombreStat):
    for stat in poke.stats:
        if stat["name"] == nombreStat:
            return stat["value"]

def getPW(self, poke, nombreMove):
    for move in poke.stats:
        if move["name"] == nombreMove:
            return move["power"]

def getPC(self, poke, nombreMove):
    for move in poke.stats:
        if move["name"] == nombreMove:
            return move["accuracy"]

def getName(self, poke):
    for name in poke.stats:
        return name["name"]

def gethp(self, pokemon):
    if pokemon == self.datos_pokemon_jugador:
        return self.hp_player
    elif pokemon == self.datos_pokemon_rival:
        return self.hp_rival

def calcularDano(self, atacante, defensor, movimiento):
    ataque = self.getStat(atacante, 'attack')
    defensa = self.getStat(defensor, 'defense')

    dano = (ataque*self.getPW(atacante, movimiento))/defensa
    return round(dano, 1)

def combate(self, movimiento_jugador, movimiento_rival):

    if self.getStat(self.datos_pokemon_jugador, 'speed') >= self.getStat(self.datos_pokemon_rival, 'speed'):
        primero = {"poke": self.datos_pokemon_jugador,
                    "move": movimiento_jugador}
        segundo = {"poke": self.datos_pokemon_rival,
                    "move": movimiento_rival}
    else:
        primero = {"poke": self.datos_pokemon_rival,
                    "move": movimiento_rival}
        segundo = {"poke": self.datos_pokemon_jugador,
                    "move": movimiento_jugador}

    # Primer ataque
    dano = self.calcularDano(
        primero["poke"], segundo["poke"], primero["move"])
    self.aplicarDano(primero, dano)

    self.log.append(
        f"{primero['poke']} usó {primero['move']} e hizo {dano} de daño.")
    self.log.append(
        f"{segundo['poke']} tiene ahora 10 PS.")

    # Segundo ataque
    if self.hp_player > 0 and self.hp_rival > 0:
        dano = self.calcularDano(
            segundo["poke"], primero["poke"], segundo["move"])
        self.aplicarDano(segundo, dano)

    self.log.append(
        f"{segundo['poke']} usó {segundo['move']} e hizo {dano} de daño.")
    self.log.append(
        f"{primero['poke']} tiene ahora 10 PS.")

def aplicarDano(self, hace, dano):
    if hace["poke"] == self.datos_pokemon_jugador:
        self.hp_rival -= dano
        if self.hp_rival < 0:
            self.hp_rival = 0
    else:
        self.hp_player -= dano
        if self.hp_player < 0:
            self.hp_player = 0

# Ejecutar un turno completo

def ejecutarTurno(self, movimiento_jugador, movimiento_rival):
    self.turno += 1
    self.log.append(f"--- Turno {self.turno} ---")

    self.combate(movimiento_jugador, movimiento_rival)

    self.mostrarLog()

def mostrarLog(self):
    for entrada in self.log:
        print(entrada)