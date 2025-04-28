from .db_connection import Database
from .tables import User

db_instance = Database()
db = db_instance.get_db()
session = db_instance.get_session()

def find_user_by_username(username):
    return User.query.filter_by(username=username).first()

def find_user_by_email(email):
    return User.query.filter_by(email=email).first()

def create_user(username, email, hashed_password):
    user = User(username=username, email=email, password_hash=hashed_password)
    session.add(user)
    session.commit()
    return user
