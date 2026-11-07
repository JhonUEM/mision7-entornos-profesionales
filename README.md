# Estimación de demanda — Misión 7

Proyecto heredado (un único `app.py`) convertido en un proyecto Python profesional:
entorno reproducible, código modular, configuración externa, validaciones, Ruff y pytest.

La estimación es la del proyecto original: **media de las ventas × factor** (por defecto 1.1).

## 1. Requisitos
- Python 3.10 o superior (`python3 --version`).
- Git.
- (Opcional) VS Code con la extensión Python.

## 2. Instalación desde cero

Linux / WSL / macOS:
Obtener el proyecto (una de las dos opciones):
```bash
# a) desde GitHub
git clone https://github.com/JhonUEM/mision7-entornos-profesionales.git
cd mision7-entornos-profesionales
# b) desde el zip de la entrega: descomprimirlo y entrar en la carpeta
cd M7_Sepulveda_Torres_Jhon
```

Crear el entorno e instalar:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install -e .
```

Windows PowerShell: igual, pero se activa con `.venv\Scripts\Activate.ps1` y se crea con `py -m venv .venv`.

Comprobar que se usa el Python del entorno (la ruta debe terminar en `.venv/...`):
```bash
python -c "import sys; print(sys.executable)"
python -m pip list
```

En VS Code: `Ctrl+Shift+P` → `Python: Select Interpreter` → `.venv`.

## 3. Configuración
```bash
cp .env.example .env
```
| Variable | Por defecto | Qué hace |
|---|---|---|
| `FACTOR_DEMANDA` | `1.1` | Multiplica la media de ventas. Debe ser un número mayor que 0. |

Si no hay `.env`, se usa 1.1. Una variable definida en la terminal tiene prioridad sobre el `.env`.

## 4. Ejecución
```bash
python -m demanda                          # usa data/ventas.csv
python -m demanda --ventas otra_ruta.csv   # otro CSV con columna "ventas"
```

## 5. Resultado esperado
```
Demanda prevista: 22.00
```
(media de 10, 20 y 30 = 20 × 1.1). Código de salida 0. Si los datos o la configuración no son válidos,
se muestra `Error: ...` y el código de salida es 1.

## 6. Pruebas y calidad
```bash
python -m pytest -q        # esperado: 11 passed
ruff check .               # esperado: All checks passed!
ruff format --check .      # esperado: N files already formatted (sin "Would reformat")
```

## 7. Estructura
```
src/demanda/
  __main__.py   entrada: argumentos, .env, mensajes y código de salida
  config.py     lee y valida FACTOR_DEMANDA
  datos.py      lee y valida el CSV
  modelo.py     lógica de negocio (sin ficheros ni prints)
tests/          pruebas pytest (modelo, datos, config)
data/ventas.csv datos de ejemplo
diagnostico.md  problemas del proyecto heredado
evidencias.md   evidencias de la misión
capturas/       capturas de las evidencias
.git/           historial de Git (en el zip): git log --oneline --graph --all
```

## 8. Problemas frecuentes
| Síntoma | Causa | Solución |
|---|---|---|
| `No module named demanda` | Falta `pip install -e .` o el entorno no está activado | Activar `.venv` y repetir el paso 2 |
| `No module named pytest` / `ruff: command not found` | Entorno no activado | `source .venv/bin/activate` |
| `Error: FACTOR_DEMANDA no es un número` | Valor mal escrito en `.env` | Poner un número con punto, p. ej. `1.1` |
| `Error: no existe el archivo` | Ruta de `--ventas` incorrecta | Revisar la ruta |
| PowerShell no deja activar el entorno | Política de ejecución | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
