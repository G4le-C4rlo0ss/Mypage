# Proyecto Registro de Usuarios

Este proyecto incluye un frontend HTML y un backend en Flask para registrar usuarios en una base de datos PostgreSQL.

## Archivos incluidos
- `index.html`: Formulario web con JavaScript para enviar datos al backend.
- `app.py`: Backend Flask para recibir y guardar usuarios en PostgreSQL.
- `requirements.txt`: Dependencias de Python.
- `.env.example`: Ejemplo de archivo con variable de entorno para la conexión a la base de datos.
- `README.md`: Este archivo con instrucciones.

## Pasos para correr el proyecto

1. Instala Python 3 y crea un entorno virtual.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Configura la variable de entorno `DATABASE_URL` con tu conexión a PostgreSQL (puedes usar Railway).
4. Crea las tablas ejecutando en consola Python:

    ```python
    from app import db
    db.create_all()
    ```
5. Corre la app con `python app.py`.
6. Cambia en `index.html` la URL `https://TU_BACKEND_URL/api/registro` por la URL donde esté corriendo tu backend (ejemplo: `https://miapp.up.railway.app/api/registro`).
7. Abre `index.html` en el navegador y prueba el formulario.

¡Listo para entregar y probar!
