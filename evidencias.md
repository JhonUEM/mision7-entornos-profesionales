# Evidencias — Jhon Mario Sepúlveda Torres (trabajo individual)

## Diagnóstico
7 problemas reproducidos; detalle en `diagnostico.md` (síntoma, causa y solución).

## Entorno
- Python: PENDIENTE (`python --version` en WSL)
- Intérprete VS Code: PENDIENTE (`.venv`, captura de la barra inferior)
- Instalación: `python -m pip install -r requirements.txt` + `python -m pip install -e .`
- Aislamiento: `python -c "import sys; print(sys.executable)"` → PENDIENTE (debe apuntar a `.venv`)
- Versiones fijadas: pytest 9.1.1, python-dotenv 1.2.4, ruff 0.16.9. Las fijé para que todos usen las mismas versiones con las que lo probé.

## Calidad
- `ruff check .` → All checks passed! · `ruff format --check .` → 8 files already formatted
- Modularización: separé lectura del CSV (`datos.py`), cálculo (`modelo.py`), configuración (`config.py`) y entrada/salida (`__main__.py`). Así la lógica se prueba sin ficheros ni prints.
- Configuración: `FACTOR_DEMANDA` desde `.env` o terminal; la terminal tiene prioridad.

## Pruebas
- 11 casos: normal, lista vacía, venta negativa, factor 0 (parámetro inválido), CSV válido, valor no numérico con línea, falta la columna, archivo inexistente, factor por defecto, factor desde el entorno y factor no numérico.
- `python -m pytest -q` → PENDIENTE (esperado 11 passed)

| Comprobación manual | Resultado | Exit |
|---|---|---|
| `python -m demanda` | Demanda prevista: 22.00 | 0 |
| ejecutar desde otra carpeta | Demanda prevista: 22.00 | 0 |
| `FACTOR_DEMANDA=1.25` | Demanda prevista: 25.00 | 0 |
| `FACTOR_DEMANDA=abc` | Error: FACTOR_DEMANDA no es un número | 1 |
| CSV vacío | Error: no hay ventas para estimar | 1 |
| CSV con -20 | Error: venta negativa no válida | 1 |

## Transferencia
Trabajo solo, así que no hay otra pareja. Como sustituto, cloné el repositorio en una carpeta limpia y seguí solo el README.
- Resultado: PENDIENTE
- Incidencias y cambios: PENDIENTE

## Colaboración
- Repositorio: https://github.com/JhonUEM/mision7-entornos-profesionales
- Rama / PR: `feature/profesionalizar` → PENDIENTE (enlace del PR)
- `git log --oneline`: PENDIENTE

## Uso de IA
Claude (Anthropic), noviembre de 2026: tutor, generación del código y de la documentación. Revisé cada archivo, ejecuté las pruebas y los casos de error yo mismo y comprobé que la cifra coincide con el proyecto original (22.0).
