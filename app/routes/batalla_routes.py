from flask import Blueprint, redirect, render_template, request, session, url_for
import app.colors as color
from app.forms.pokemon_form import PokemonForm
from app.services import battle_service
from app.services import pokemon_services
from app.repositories import pokemon_Repo
from app.models import pokemon

batalla_pb = Blueprint('batalla_route', __name__, template_folder='templates')


@batalla_pb.route('/pokedexSeleccion/', methods=["POST", "GET"])
def PokedexS():
    form = PokemonForm()

    if form.validate_on_submit():
        session["pokemon"] = form.pokemon.data
        return redirect(url_for('batalla_route.BatallaP'))

    nombre = session.get("trainer")
    return render_template('pickPokemon.html', pokemons=pokemon_services.listar_pokemons(), colorM=color.colorT, nombreUser=nombre, form=form)


@batalla_pb.route('/batallasPokemon', methods=["POST", "GET"])
def BatallaP():

    nombrePokemon = session.get("pokemon")

    if not nombrePokemon:
        return redirect(url_for('batalla_route.PokedexS'))

    pokemons = pokemon_services.listar_pokemons()

    # mensaje = ""
    # if name != nombre:
    #     mensaje = "El pokemon "+name+" no se encuentra en la pokedex."
    #     return render_template("error404.html", mensaje=mensaje), 404

    # Pokemons aleatorios de contrincante
    pokemonContrincante = battle_service.pokemonContrincante()

    # Pokemon elegido por el jugador
    pokemonJugadorUnico = battle_service.pokemonJugador(nombrePokemon)

    if pokemonJugadorUnico == None:
        mensaje = "El pokemon "+nombrePokemon + \
            " no se encuentra en la lista de la Pokedex."
        return render_template("error404.html", mensaje=mensaje), 404

    movimientos = battle_service.movimientosJugador(pokemonJugadorUnico)
    movimientoRival = battle_service.movimientosContrincante(
        pokemonContrincante)

    if "batalla" not in session:
        batalla = pokemon.Batalla(pokemonJugadorUnico, pokemonContrincante)
        # Nota: objetos complejos no se guardan directamente, se debe usar pickle o guardar solo datos necesarios
        session["batalla"] = batalla
    else:
        batalla = session["batalla"]

    movimientoDelTurno = request.form.get('movimiento')

    return render_template('batalla.html', pokemons=pokemons, pokemonContrincante=pokemonContrincante, pokemonJugadorUnico=pokemonJugadorUnico, colorM=color.colorM, nombrePokemon=nombrePokemon, movimientos=movimientos, batalla=batalla)


@batalla_pb.route("/test")
def listar_productos():
    conn = pokemon_Repo.get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, precio FROM productos ORDER BY id;")

    productos = cur.fetchall()

    cur.close()
    conn.close()
    return render_template("productos.html", productos=productos)
