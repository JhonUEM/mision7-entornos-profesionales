# Diagnóstico del proyecto heredado

Ejecuté el `app.py` original con Python 3.13 y lo probé con varios CSV. Funciona solo en el caso feliz y
desde su propia carpeta.

| # | Problema | Cómo se reproduce | Causa | Solución aplicada |
|---|---|---|---|---|
| 1 | Ruta fija | `cd /tmp && python ruta/app.py` → `FileNotFoundError: 'ventas.csv'` (exit 1) | `ARCHIVO = 'ventas.csv'` es relativa a la carpeta desde la que se ejecuta | Ruta por defecto relativa al proyecto y parámetro `--ventas` |
| 2 | CSV vacío | CSV solo con cabecera → `ZeroDivisionError` (exit 1) | `estimar()` divide por `len(valores)` sin comprobar | `ValueError("no hay ventas para estimar")` |
| 3 | Valor no numérico | fila `abc` → `ValueError: could not convert string to float` sin indicar dónde | `float()` sin validación | Error con número de línea: `línea 3: valor no numérico 'abc'` |
| 4 | Negativos aceptados | ventas 10 y -20 → `Demanda prevista: -5.5` (exit 0) | No valida el dominio | Se rechazan ventas negativas |
| 5 | Número mágico | `1.1` escrito dentro de `estimar()` | Configuración mezclada con la lógica | Variable `FACTOR_DEMANDA` (`.env`), validada (> 0) |
| 6 | Lógica y E/S mezcladas | `ejecutar()` lee el fichero, calcula e imprime | Sin separar responsabilidades | `datos.py` (lectura), `modelo.py` (cálculo), `__main__.py` (entrada/salida) |
| 7 | No reproducible ni probado | No hay `requirements.txt`, `.gitignore`, pruebas ni README útil | Proyecto de un solo fichero | Entorno `.venv`, versiones fijadas, 11 pruebas pytest, Ruff y README |

Salida original de referencia: `Demanda prevista: 22.0`. El nuevo proyecto da el mismo valor (`22.00`).
