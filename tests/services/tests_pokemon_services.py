from unittest.mock import patch
import app.repositories.pokemon_Repo as pokemon_repo
from app.services.pokemon_services import listar_pokemons


def test_listar_pokemons():
    pokemons_mock = ["p1", "p2"]

    with patch(
        "app.services.pokemon_services.pokemon_repo.obtener_Pokemons"
    ) as mock_repo:
        mock_repo.return_value = pokemons_mock

        resultado = listar_pokemons()

        assert resultado == pokemons_mock
        mock_repo.assert_called_once()

# def obtener_pokemon_por_id(id):

#     if id < 0 or id is None:
#         return None
    
#     return pokemon_repo.buscar_por_id(id)