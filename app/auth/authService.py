from flask_bcrypt import Bcrypt
from flask_login import logout_user
from ..models.queries import find_user_by_username, find_user_by_email, create_user

bcrypt = Bcrypt()

class AuthService:
    @staticmethod
    def login(username, password):
        try:
            user = find_user_by_username(username)
            if user and bcrypt.check_password_hash(user.password_hash, password):
                return user
            return None
        except Exception as e:
            print(f"Error during login: {e}")
            return None

    @staticmethod
    def register(username, email, password):
        try:
            if find_user_by_username(username):
                raise ValueError("Username already exists.")
            if find_user_by_email(email):
                raise ValueError("Email already exists.")
            hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
            return create_user(username, email, hashed_pw)
        except ValueError as e:
            raise e
        except Exception as e:
            print(f"Error during registration: {e}")
            raise Exception("An error occurred while creating your account.")

    @staticmethod
    def logout():
        logout_user()
