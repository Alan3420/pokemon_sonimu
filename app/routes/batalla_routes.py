import random
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
import app.colors as color
from app.forms.pokemon_form import PokemonForm
from app.repositories.batallas_Repo import crear_batalla
from app.repositories.entrenador_Repo import obtener_entrenador_por_nombre, obtener_todos_los_entrenadores
from app.services import battle_service
from app.services import pokemon_services
from app.models.batalla import Batalla
import app.models.exceptions as Exception


batalla_pb = Blueprint('batalla_route', __name__, template_folder='templates')


@batalla_pb.route('/pokedexSeleccion/', methods=["POST", "GET"])
def PokedexS():
    form = PokemonForm()

    if form.validate_on_submit():
        session.pop("batalla", None)
        session["pokemon"] = form.pokemon.data
        return redirect(url_for('batalla_route.BatallaP'))

    nombre = session["trainer"]
    return render_template('pickPokemon.html', pokemons=pokemon_services.listar_pokemons(), colorM=color.colorT, nombreUser=nombre, form=form)


@batalla_pb.route('/batallasPokemon', methods=["POST", "GET"])
def BatallaP():
    fin = False
    resultado = ''
    orden_ataques = ''
    nombrePokemon = session.get("pokemon")

    if not nombrePokemon:
        return redirect(url_for('batalla_route.PokedexS'))

    pokemons = pokemon_services.listar_pokemons()

    # Pokemons aleatorios de contrincante
    pokemonContrincante = battle_service.pokemonContrincante()

    # Pokemon elegido por el jugador
    pokemonJugadorUnico = battle_service.pokemonJugador(nombrePokemon)

    try:
        if pokemonJugadorUnico is None:
            raise Exception.PokemonNoEncontrado(
                f"El Pokémon {nombrePokemon} no se encuentra en la Pokedex."
            )

    except Exception.PokemonNoEncontrado as e:
        return render_template("error404.html", mensaje=str(e)), 404

    hp_Jugador = Batalla.get_stat(pokemonJugadorUnico, "hp")
    hp_rival = Batalla.get_stat(pokemonContrincante, "hp")

    movimientosJugador = battle_service.movimientosJugador(pokemonJugadorUnico)
    movimientosRival = battle_service.movimientosContrincante(
        pokemonContrincante)

    num_sini = random.randint(1, 1000)

    if "batalla" not in session:
        batalla = Batalla(pokemonJugadorUnico, movimientosJugador,
                          hp_Jugador, pokemonContrincante, movimientosRival, hp_rival, num_sini)
        session["batalla"] = batalla.to_dict()

    else:
        datos = session["batalla"]
        # Comprobacion por si el pokemon esta en sesion, reiniciar la batalla
        if pokemonJugadorUnico.name == datos["datos_pokemon_jugador"].name:
            batalla = Batalla(
                datos_pokemon_jugador=datos["datos_pokemon_jugador"],
                movimientosJugador=datos["movimientosJugador"],
                hp_Jugador=datos["hp_Jugador"],
                datos_pokemon_rival=datos["datos_pokemon_rival"],
                movimientosRival=datos["movimientosRival"],
                hp_rival=datos["hp_rival"],
                prob_shiny=datos["prob_shiny"],
                turno=datos["turno"],
                log=datos["log"]

            )

        else:
            batalla = Batalla(pokemonJugadorUnico, movimientosJugador,
                              hp_Jugador, pokemonContrincante, movimientosRival, hp_rival)
            session["batalla"] = batalla.to_dict()

    # Recoger los datos de las sesion
    pokemonJugadorUnico = batalla.datos_pokemon_jugador
    hp_Jugador = batalla.hp_Jugador
    hp_max_jugador = batalla.get_stat(pokemonJugadorUnico, "hp")
    movimientosJ = batalla.movimientosJugador
    pokemonContrincante = batalla.datos_pokemon_rival
    movimientoR = batalla.movimientosRival
    hp_rival = batalla.hp_rival
    hp_max_rival = batalla.get_stat(pokemonContrincante, "hp")
    log = batalla.log
    turno = batalla.turno
    num_sini = batalla.prob_shiny

    # Ejecucion de los movimientos
    if request.method == "POST":
        movimiento_usado = request.form.get("movimiento")
        movimiento_usado_rival = random.choice(movimientoR)["name"]
        hp_Jugador, hp_rival, turno, resultado, orden_ataques = battle_service.ejecutarTurno(
            pokemonJugadorUnico,
            pokemonContrincante,
            movimiento_usado,
            hp_Jugador,
            movimiento_usado_rival,
            hp_rival,
            turno,
            log
        )

        if hp_rival <= 0:
            batalla.hp_rival = 0
            batalla.hp_Jugador = hp_Jugador
            fin = True
        elif hp_Jugador <= 0:
            batalla.hp_Jugador = 0
            batalla.hp_rival = hp_rival
            fin = True
        else:
            batalla.hp_rival = hp_rival
            batalla.hp_Jugador = hp_Jugador
            batalla.turno = turno

    # devolver datos a la sesion
    session["batalla"] = batalla.to_dict()

    if fin == True:
        resul = None
        # CRECION DE LA BATALLA EN LA BD
        entrenador_dict = session["trainer"]
        entrenadorJugador = obtener_entrenador_por_nombre(
            entrenador_dict["nombre"])

        todos_entrenadores = obtener_todos_los_entrenadores()
        contrincantes = [
            e for e in todos_entrenadores if e.id != entrenadorJugador.id]

        if contrincantes:
            contrincante = random.choice(contrincantes)

        if hp_Jugador == 0:
            resul = 1

        else:
            resul = 0

        crear_batalla(id_entrenador1=entrenadorJugador.id, id_pokemon1=pokemonJugadorUnico.id,
                      id_entrenador2=contrincante.id, id_pokemon2=pokemonContrincante.id, resultado=resul)

    return render_template('batalla.html', pokemons=pokemons, pokemonContrincante=pokemonContrincante, hp_rival=hp_rival, hp_max_rival=hp_max_rival, pokemonJugadorUnico=pokemonJugadorUnico, hp_Jugador=hp_Jugador, hp_max_jugador=hp_max_jugador, colorM=color.colorM, nombrePokemon=nombrePokemon, movimientos=movimientosJ, batalla=batalla, log=log, resultado=resultado, orden_ataques=orden_ataques, num_sini_lokete=num_sini)
