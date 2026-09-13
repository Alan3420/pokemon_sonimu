from unittest.mock import patch
from app.services.trainer_service import registrar_entrenador


def test_registrar_entrenador_nuevo():
    with patch(
        "app.services.trainer_service.obtener_entrenador_por_nombre",
        return_value=None
    ), patch(
        "app.services.trainer_service.crear_entrenador"
    ) as mock_crear:

        assert registrar_entrenador("Ash", "pikachu") is True
        mock_crear.assert_called_once_with("Ash", "pikachu")


def test_registrar_entrenador_con_nombre_en_uso():
    with patch(
        "app.services.trainer_service.obtener_entrenador_por_nombre",
        return_value=object()
    ), patch(
        "app.services.trainer_service.crear_entrenador"
    ) as mock_crear:

        assert registrar_entrenador("Ash", "otra") is False
        mock_crear.assert_not_called()
