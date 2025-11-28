from flask import Blueprint, current_app, render_template
import app.colors as color
from app.services import pokemon_services
import app.models.exceptions as Exception

pokedex_pb = Blueprint('pokedex_route',__name__,template_folder='templates')

@pokedex_pb.route('/')
def Pokedex():

    return render_template('pokemons.html', pokemons = pokemon_services.listar_pokemons(), colorM=color.colorT)

@pokedex_pb.route('/<int:id>/')
def PokedexDetails(id):

    try:
        idPokemon = pokemon_services.obtener_pokemon_por_id(id)
        if idPokemon is None:
            raise Exception.PokemonNoEncontrado(
                f"El Pokémon no se encuentra en la Pokedex."
            )
    except Exception.PokemonNoEncontrado as e:
        return render_template("error404.html", mensaje=str(e)), 404

    return render_template('pokemonsID.html', pokemon = idPokemon, colorM = color.colorM)