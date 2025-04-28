# 📦 Plantilla Flask 

Este proyecto es una **plantilla base** para crear aplicaciones web en **Flask** (Python) y desplegarlas fácilmente en **Render** utilizando el plan gratuito.

La estructura está preparada para:

- Flask modularizado (separación de carpetas).
- Base de datos SQLite.
- Autenticación de usuarios básica.
- Entorno de producción usando `gunicorn`.
- Variables de entorno configurables.
- Despliegue automático en Render vía GitHub.

---

## 🚀 Tecnologías utilizadas

- **Python 3.10+**
- **Flask**
- **Flask-Login**
- **Flask-SQLAlchemy**
- **gunicorn** (servidor de producción)

---

## 📂 Estructura del proyecto

```plaintext
/app/                 # Código principal de la app Flask
   __init__.py        # Inicializa Flask, DB y LoginManager
   /auth/             # Controladores de autenticación
   /models/           # Modelos de base de datos
   /templates/        # Plantillas HTML
   /static/           # Archivos estáticos (CSS, JS, imágenes)

/instance/            # Archivos como la base de datos SQLite (no se sube a GitHub)

run.py                # Arranque local de la app
requirements.txt      # Dependencias del proyecto
Procfile              # Instrucciones para Render
.gitignore            # Ignora la base de datos y archivos temporales
README.md             # Este archivo
