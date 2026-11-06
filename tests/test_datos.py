import pytest

from demanda.datos import leer_ventas


def test_lee_csv_valido(tmp_path):
    ruta = tmp_path / "ok.csv"
    ruta.write_text("ventas\n10\n20\n", encoding="utf-8")
    assert leer_ventas(ruta) == [10.0, 20.0]


def test_valor_no_numerico_indica_linea(tmp_path):
    ruta = tmp_path / "malo.csv"
    ruta.write_text("ventas\n10\nabc\n", encoding="utf-8")
    with pytest.raises(ValueError, match="línea 3"):
        leer_ventas(ruta)


def test_falta_columna_ventas(tmp_path):
    ruta = tmp_path / "sin.csv"
    ruta.write_text("unidades\n10\n", encoding="utf-8")
    with pytest.raises(ValueError, match="columna 'ventas'"):
        leer_ventas(ruta)


def test_archivo_inexistente(tmp_path):
    with pytest.raises(FileNotFoundError):
        leer_ventas(tmp_path / "no_existe.csv")
