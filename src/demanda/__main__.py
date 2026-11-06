import argparse
import sys
from pathlib import Path

from dotenv import load_dotenv

from demanda.config import factor_demanda
from demanda.datos import leer_ventas
from demanda.modelo import estimar

RAIZ = Path(__file__).resolve().parents[2]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Estima la demanda prevista.")
    parser.add_argument(
        "--ventas",
        type=Path,
        default=RAIZ / "data" / "ventas.csv",
        help="CSV con una columna 'ventas'",
    )
    args = parser.parse_args(argv)
    load_dotenv(RAIZ / ".env")  # no pisa variables ya definidas
    try:
        previsto = estimar(leer_ventas(args.ventas), factor_demanda())
    except (ValueError, FileNotFoundError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    print(f"Demanda prevista: {previsto:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
