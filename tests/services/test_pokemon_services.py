from unittest.mock import patch
from app.services.pokemon_services import listar_pokemons


def test_listar_pokemons_sin_datos_devuelve_lista_vacia():
    with patch(
        "app.services.pokemon_services.pokemonClient.get_pokemons"
    ) as mock_client:
        mock_client.return_value = None

        resultado = listar_pokemons()

        assert resultado == []
        mock_client.assert_called_once_with(5, 1)


def test_listar_pokemons_omite_pokemon_no_encontrado():
    listado = {"results": [{"url": "https://pokeapi.co/api/v2/pokemon/25/"}]}

    with patch(
        "app.services.pokemon_services.pokemonClient.get_pokemons",
        return_value=listado
    ), patch(
        "app.services.pokemon_services.pokemonClient.get_pokemon",
        return_value=None
    ) as mock_detalle:

        resultado = listar_pokemons()

        assert resultado == []
        mock_detalle.assert_called_once_with(25)
