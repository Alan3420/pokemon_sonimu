import random
from flask import Blueprint, redirect, render_template, request, session, url_for
import app.colors as color
from app.forms.pokemon_form import PokemonForm
from app.services import battle_service
from app.services import pokemon_services

batalla_pb = Blueprint('batalla_route', __name__, template_folder='templates')


@batalla_pb.route('/pokedexSeleccion/', methods=["POST", "GET"])
def PokedexS():
    form = PokemonForm()

    if form.validate_on_submit():
        session["pokemon"] = form.pokemon.data
        return redirect(url_for('batalla_route.BatallaP'))

    nombre = session.get("trainer")
    return render_template('pickPokemon.html', pokemons=pokemon_services.listar_pokemons(), colorM=color.colorT, nombreUser=nombre, form=form)


@batalla_pb.route('/batallasPokemon/<name>/', methods=["POST", "GET"])
def BatallaP(name):

    nombre = session.get("pokemon")
    pokemons = pokemon_services.listar_pokemons()

    # Pokemons aleatorios de contrincante
    pokemonContrincante = battle_service.pokemonContrincante()

    # Pokemon elegido por el jugador
    pokemonJugadorUnico = battle_service.pokemonJugador(name)
    movimientos = battle_service.movimientosJugador(pokemonJugadorUnico)

    return render_template('batalla.html', pokemons=pokemons, pokemonContrincante=pokemonContrincante, pokemonJugadorUnico=pokemonJugadorUnico, colorM=color.colorM, nombrePokemon=nombre, movimientos=movimientos)
