# Demo aislada (mock)

Pequeño ejemplo con Django para ilustrar conceptos usados en el **Proyecto X** sin exponer código propietario.

## Requisitos
- Python 3.10+
- pip

## Pasos
```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata seeds.json   # datos de ejemplo
python manage.py runserver
```

Abrir: http://127.0.0.1:8000/

## Qué muestra
- Listado de productos (modelo simple)
- Importación mock desde CSV (vista simplificada)
- Validaciones básicas y mensajes de resultado
