from flask import Blueprint, current_app, render_template, request, session
import app.colors as color
from app.services import pokemon_services
import app.models.exceptions as Exception

pokedex_pb = Blueprint('pokedex_route',__name__,template_folder='templates')

@pokedex_pb.route('/')
def Pokedex():
    usuario = session.get("trainer")

    # Obtener parámetros de paginación
    pagina = request.args.get('page', 1, type=int)
    limite = request.args.get('limit', 2, type=int)  # Por defecto 2 pokémons
    
    # Obtener todos los pokémons
    todos_pokemons = pokemon_services.listar_pokemons()

    # Calcular índices para la paginación
    total = len(todos_pokemons)
    start = (pagina - 1) * limite
    end = start + limite

    # Obtener pokémons de la página actual
    pokemons_pagina = todos_pokemons[start:end]

    # Calcular número total de páginas
    total_pages = (total / limite) #limite
    prev_page = None
    next_page = None
    if pagina > 1:
        prev_page = pagina - 1
    else:
        prev_page = None
    
    if pagina < total_pages: 
        next_page = pagina + 1 
    else:
        next_page = None   

    pagination = {
        'page': pagina,
        'total': total,
        'total_pages': total_pages,
        'prev_page': prev_page,
        'next_page': next_page
    }

    return render_template('pokemons.html',  pokemons=pokemons_pagina, colorM=color.colorT, usuario=usuario, pagination=pagination)

    #return render_template('pokemons.html', pokemons = pokemon_services.listar_pokemons(), colorM=color.colorT, usuario = usuario)

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