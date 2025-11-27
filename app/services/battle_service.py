import random

import app.repositories.pokemon_Repo as pokemon_repo
from app.services import pokemon_services
from app.models.batalla import Batalla


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

# Logica de batalla
def ejecutarTurno(pokemonJugador, pokemonRival, habilidadJugador, hp_Jugador, habilidadRival, hp_rival,turno, log):        
    turno +=1
    resultado = None  
    bloque = []
    bloque.append(f"___ Turno {turno} ___")

    if Batalla.get_stat(pokemonJugador, "speed") >= Batalla.get_stat(pokemonRival, "speed"):
        primero = {
            "name": pokemonJugador,
            "habilidad": habilidadJugador,
            "hp": hp_Jugador
        }
        segundo = {
            "name": pokemonRival,
            "habilidad": habilidadRival,
            "hp": hp_rival
        }
    else :
        primero = {
            "name": pokemonRival,
            "habilidad": habilidadRival,
            "hp": hp_rival
        }
        segundo = {
            "name": pokemonJugador,
            "habilidad": habilidadJugador,
            "hp": hp_Jugador
        }

    dano = calcularDano(primero["name"], primero["habilidad"], segundo["name"])
    segundo["hp"] -= dano

    bloque.append(f"1º: {primero['name'].name} usó {primero['habilidad']} e hizo {dano} de daño. {segundo['name'].name} tiene ahora {max(0, segundo['hp'])} PS.")
    
    if segundo['hp'] > 0:
        dano = calcularDano(segundo["name"], segundo["habilidad"], primero["name"])
        primero["hp"] -= dano

        bloque.append(f"2º: {segundo['name'].name} usó {segundo['habilidad']} e hizo {dano} de daño. {primero['name'].name} tiene ahora {max(0,primero['hp'])} PS.")
        
    log.insert(0, bloque)
    if primero["name"].name == pokemonJugador.name:

        if segundo["hp"] < 0:
            resultado ="Ganado"
        elif primero["hp"] < 0:
            resultado="Perdido"

        return primero["hp"], segundo["hp"], turno, resultado
    else:
        if segundo["hp"] < 0:
            resultado ="Perdido"
        elif primero["hp"] < 0:
            resultado="Ganado"

        return segundo["hp"], primero["hp"], turno, resultado      
def calcularDano(pokemonAtaque , habilidad, pokemonAtacado):
    ataque =  Batalla.get_stat(pokemonAtaque, 'attack')
    defensa = Batalla.get_stat(pokemonAtacado, 'defense')

        
    power = get_move_stat(pokemonAtaque, habilidad, "power")
    dano = int((power * (ataque / defensa)) / 4) + 1
    return int(dano)

def get_move_stat(pokemon, move_name, key):
    for move in pokemon.moves:
        if move["name"] == move_name:
            return move.get(key)
    return None
# Fin logica de batalla