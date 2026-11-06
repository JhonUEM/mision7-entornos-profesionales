import pytest

from demanda.modelo import estimar


def test_caso_normal():
    assert estimar([10, 20, 30]) == pytest.approx(22.0)


def test_lista_vacia_da_error():
    with pytest.raises(ValueError, match="no hay ventas"):
        estimar([])


def test_venta_negativa_da_error():
    with pytest.raises(ValueError, match="negativa"):
        estimar([10, -20])


def test_factor_invalido_da_error():
    with pytest.raises(ValueError, match="mayor que 0"):
        estimar([10], factor=0)
