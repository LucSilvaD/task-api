# Inventory API

Mini API para gestionar un inventario de productos, desarrollada como proyecto base del curso de Metodologías de Desarrollo.

## Objetivo del proyecto
Construir una aplicación pequeña que permita practicar flujo de trabajo moderno con Python, Git, GitHub y FastAPI, adaptando el dominio original (Tareas) a un sistema de inventario.

## Funcionalidades iniciales
- Listar productos disponibles.
- Crear nuevos productos (con nombre, descripción y precio).
- Marcar productos como "sin stock".

## Tecnologías utilizadas
- Python
- FastAPI
- Uvicorn
- Pydantic
- Git
- GitHub

## Estructura del proyecto
`task-api/`

│── `app/`

│ └── `main.py`

│── `docs/`

│── `tests/`

│── `README.md`

│── `requirements.txt`

## Ejecución local
1. Crear entorno virtual:
    - `python -m venv venv`

2. Activar entorno virtual:
    - En Windows Powershell: `.\venv\Scripts\Activate.ps1`

3. Instalar dependencias:
    - `pip install -r requirements.txt`

4. Ejecutar la API:
    - `uvicorn app.main:app --reload`

5. Abrir documentación interactiva:
    - http://127.0.0.1:8000/docs
