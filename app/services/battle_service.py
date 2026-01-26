import random
from app.services import pokemon_services
from app.models.batalla import Batalla


def pokemonContrincante():
    id = random.randint(1, 1025)
    print(id)
    pokemon = pokemon_services.obtener_pokemon_por_id(id)
    return pokemon


def movimientosContrincante(pokemonContrincanteUnico):

    # Si el jugador a seleccionado un pokemon se cargaran su sets de movimientos de forma aleatoria
    if pokemonContrincanteUnico != None:
        movimientos = random.sample(pokemonContrincanteUnico.moves, 4)

    return movimientos


def pokemonJugador(name):
    nombre = name.strip().lower()
    pokemon = pokemon_services.obtener_pokemon_por_name(nombre)
    print("Jugador"+name)
    return pokemon

def movimientosJugador(pokemonJugadorUnico):

    # Si el jugador a seleccionado un pokemon se cargaran su sets de movimientos de forma aleatoria
    if pokemonJugadorUnico != None:
        movimientos = random.sample(pokemonJugadorUnico.moves, 4)

    return movimientos

# Logica de batalla


def ejecutarTurno(pokemonJugador, pokemonRival, habilidadJugador, hp_Jugador, habilidadRival, hp_rival, turno, log):
    turno += 1
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
    else:
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

    orde_ataques = []

    dano, mult, hit = calcularDano(
        primero["name"], primero["habilidad"], segundo["name"])
    if mult > 1:
        efecto = "¡Es super efectivo!"
    elif mult < 1:
        efecto = "No es muy efectivo..."
    else:
        efecto = ""

    if hit:
        segundo["hp"] -= dano

        bloque.append(
            f"1º: {primero['name'].name} usó {primero['habilidad']}, el ataque {efecto} hizo {dano} de daño. {segundo['name'].name} tiene ahora {max(0, segundo['hp'])} PS.")
    else:
        bloque.append(
            f"1º: {primero['name'].name} usó {primero['habilidad']}, el ataque fallo")

    # Asi identifico a quien poner la animacion
    orde_ataques.append(primero["name"].name)
    if segundo['hp'] > 0:
        dano, mult, hit = calcularDano(
            segundo["name"], segundo["habilidad"], primero["name"])
        if mult > 1:
            efecto = "¡Es super efectivo!"
        elif mult < 1:
            efecto = "no es muy efectivo..."
        else:
            efecto = ""

        if hit:
            primero["hp"] -= dano

            bloque.append(
                f"2º: {segundo['name'].name} usó {segundo['habilidad']}, el ataque {efecto} e hizo {dano} de daño. {primero['name'].name} tiene ahora {max(0, primero['hp'])} PS.")
        else:
            bloque.append(
                f"2º: {segundo['name'].name} usó {segundo['habilidad']},pero el ataque fallo")

        # Por si ataque despues
    orde_ataques.append(segundo["name"].name)

    log.insert(0, bloque)
    if primero["name"].name == pokemonJugador.name:

        if segundo["hp"] < 0:
            resultado = "Ganado"
        elif primero["hp"] < 0:
            resultado = "Perdido"

        return primero["hp"], segundo["hp"], turno, resultado, orde_ataques
    else:
        if segundo["hp"] < 0:
            resultado = "Perdido"
        elif primero["hp"] < 0:
            resultado = "Ganado"

        return segundo["hp"], primero["hp"], turno, resultado, orde_ataques


def efectividad(move_tipo, defensor_tipos):
    mult = 1.0
    for tipo in defensor_tipos:
        mult *= type_chart.get(move_tipo, {}).get(tipo, 1.0)
    return mult


def calcularDano(pokemonAtaque, habilidad, pokemonAtacado):
    ataque = Batalla.get_stat(pokemonAtaque, 'attack')
    defensa = Batalla.get_stat(pokemonAtacado, 'defense')
    precision = get_move_stat(pokemonAtaque, habilidad, 'accuracy')
    if precision == None:
        precision = 0
    mult = efectividad(get_move_stat(
        pokemonAtaque, habilidad, "type"), pokemonAtacado.types)

    power = get_move_stat(pokemonAtaque, habilidad, "power")
    if power == None:
        power = 0
    dano = int((power * (ataque / defensa) * mult) / 4) + 1

    prob = random.uniform(0, 1)

    hit = False

    if precision/100 > prob:
        hit = True

    return int(dano), mult, hit


def get_move_stat(pokemon, move_name, key):
    for move in pokemon.moves:
        if move["name"] == move_name:
            return move.get(key)
    return None
# Fin logica de batalla


# Esto esta robado, todos los creditos a mi primo
type_chart = {
    "normal": {"rock": 0.5, "ghost": 0, "steel": 0.5},
    "fire": {"fire": 0.5, "water": 0.5, "grass": 2, "ice": 2, "bug": 2, "rock": 0.5, "dragon": 0.5, "steel": 2},
    "water": {"fire": 2, "water": 0.5, "grass": 0.5, "ground": 2, "rock": 2, "dragon": 0.5},
    "electric": {"water": 2, "electric": 0.5, "ground": 0, "flying": 2, "dragon": 0.5},
    "grass": {"fire": 0.5, "water": 2, "grass": 0.5, "poison": 0.5, "ground": 2, "flying": 0.5, "rock": 2, "bug": 0.5, "dragon": 0.5, "steel": 0.5},
    "ice": {"fire": 0.5, "water": 0.5, "grass": 2, "ice": 0.5, "ground": 2, "flying": 2, "dragon": 2, "steel": 0.5},
    "fighting": {"normal": 2, "ice": 2, "rock": 2, "dark": 2, "steel": 2, "poison": 0.5, "flying": 0.5, "psychic": 0.5, "bug": 0.5, "ghost": 0},
    "poison": {"grass": 2, "poison": 0.5, "ground": 0.5, "rock": 0.5, "ghost": 0.5, "steel": 0},
    "ground": {"fire": 2, "electric": 2, "grass": 0.5, "poison": 2, "flying": 0, "bug": 0.5, "rock": 2, "steel": 2},
    "flying": {"electric": 0.5, "grass": 2, "fighting": 2, "bug": 2, "rock": 0.5, "steel": 0.5},
    "psychic": {"fighting": 2, "poison": 2, "psychic": 0.5, "dark": 0},
    "bug": {"fire": 0.5, "grass": 2, "fighting": 0.5, "poison": 0.5, "flying": 0.5, "psychic": 2, "ghost": 0.5, "dark": 2, "steel": 0.5, "fairy": 0.5},
    "rock": {"fire": 2, "ice": 2, "fighting": 0.5, "ground": 0.5, "flying": 2, "bug": 2, "steel": 0.5},
    "ghost": {"normal": 0, "psychic": 2, "ghost": 2, "dark": 0.5},
    "dragon": {"dragon": 2, "steel": 0.5, "fairy": 0},
    "dark": {"fighting": 0.5, "psychic": 2, "ghost": 2, "dark": 0.5, "fairy": 0.5},
    "steel": {"fire": 0.5, "water": 0.5, "electric": 0.5, "ice": 2, "rock": 2, "fairy": 2, "steel": 0.5},
    "fairy": {"fire": 0.5, "fighting": 2, "poison": 0.5, "dragon": 2, "dark": 2, "steel": 0.5},
}
