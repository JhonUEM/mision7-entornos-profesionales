import pytest

from demanda.config import factor_demanda


def test_factor_por_defecto(monkeypatch):
    monkeypatch.delenv("FACTOR_DEMANDA", raising=False)
    assert factor_demanda() == pytest.approx(1.1)


def test_factor_desde_entorno(monkeypatch):
    monkeypatch.setenv("FACTOR_DEMANDA", "1.25")
    assert factor_demanda() == pytest.approx(1.25)


def test_factor_no_numerico(monkeypatch):
    monkeypatch.setenv("FACTOR_DEMANDA", "mucho")
    with pytest.raises(ValueError, match="no es un número"):
        factor_demanda()
