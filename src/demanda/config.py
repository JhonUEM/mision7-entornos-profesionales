import os

FACTOR_POR_DEFECTO = 1.1


def factor_demanda():
    """Lee FACTOR_DEMANDA del entorno y devuelve el factor."""
    valor = os.getenv("FACTOR_DEMANDA", str(FACTOR_POR_DEFECTO))
    try:
        factor = float(valor)
    except ValueError:
        raise ValueError(f"FACTOR_DEMANDA no es un número: {valor!r}") from None
    if factor <= 0:
        raise ValueError(f"FACTOR_DEMANDA debe ser mayor que 0: {factor}")
    return factor
