from flask_login import UserMixin
from .db_connection import Database

db = Database().get_db()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
