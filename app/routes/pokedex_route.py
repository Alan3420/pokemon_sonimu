from flask import Blueprint, current_app, render_template, request
import colors as color
from app.services import pokemon_services

pokedex_pb = Blueprint('pokedex_route',__name__,template_folder='templates')

@pokedex_pb.route('/')
def Pokedex():
    
    
    return render_template('pokemons.html', pokemons = current_app.config["data"], colorM=color.colorT)

@pokedex_pb.route('/<int:id>/')
def PokedexDetails(id):

    idPokemon = pokemon_services.obtener_pokemon_por_id(id)


    return render_template('pokemonsID.html', pokemon = idPokemon, colorM = color.colorM)