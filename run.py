# run.py
from app import create_app
from app.models.db_connection import Database

app = create_app()

# Crear las tablas en el contexto de la app
with app.app_context():
    db_instance = Database()
    db = db_instance.get_db()
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
