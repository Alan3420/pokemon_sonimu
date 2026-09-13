from unittest.mock import patch
from app.clients.pokemon_clients import PokemonJsonClient


def test_cache_devuelve_valor_guardado():
    client = PokemonJsonClient()
    client._set_cache("pikachu", {"id": 25})

    assert client._get_cache("pikachu") == {"id": 25}


def test_cache_no_supera_el_maximo():
    client = PokemonJsonClient()
    client.maxima_Cache = 3

    for i in range(5):
        client._set_cache(i, i)

    assert len(client._cache) == 3
    assert list(client._cache.keys()) == [2, 3, 4]


def test_cache_elimina_el_menos_usado_recientemente():
    client = PokemonJsonClient()
    client.maxima_Cache = 2
    client._set_cache("a", 1)
    client._set_cache("b", 2)

    client._get_cache("a")
    client._set_cache("c", 3)

    assert "a" in client._cache
    assert "b" not in client._cache


def test_cache_actualiza_clave_existente():
    client = PokemonJsonClient()
    client._set_cache("a", 1)
    client._set_cache("b", 2)

    client._set_cache("a", 10)

    assert client._get_cache("a") == 10
    assert list(client._cache.keys()) == ["b", "a"]


def test_cache_expira_tras_ttl():
    client = PokemonJsonClient()

    with patch("app.clients.pokemon_clients.time.time", return_value=1000):
        client._set_cache("a", 1)

    with patch("app.clients.pokemon_clients.time.time", return_value=1000 + client.TTL + 1):
        assert client._get_cache("a") is None
        assert "a" not in client._cache
