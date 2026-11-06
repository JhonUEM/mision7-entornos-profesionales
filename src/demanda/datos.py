import csv
from pathlib import Path


def leer_ventas(ruta):
    """Lee la columna 'ventas' de un CSV y devuelve una lista de números."""
    ruta = Path(ruta)
    if not ruta.is_file():
        raise FileNotFoundError(f"no existe el archivo: {ruta}")
    ventas = []
    with ruta.open(encoding="utf-8", newline="") as f:
        lector = csv.DictReader(f)
        if not lector.fieldnames or "ventas" not in lector.fieldnames:
            raise ValueError("el CSV debe tener una columna 'ventas'")
        for num_linea, fila in enumerate(lector, start=2):
            texto = (fila["ventas"] or "").strip()
            try:
                ventas.append(float(texto))
            except ValueError:
                raise ValueError(
                    f"línea {num_linea}: valor no numérico {texto!r}"
                ) from None
    return ventas
