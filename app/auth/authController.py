# authController.py
from flask import flash
from .authService import AuthService

class AuthController:
    @staticmethod
    def login(username, password):
        try:
            user = AuthService.login(username, password)
            if user:
                flash('Inicio de sesión correcto!', 'success')
                return user
            else:
                flash('Inicio de sesión fallido. Comprueba tus datos.', 'danger')
                return None
        except Exception as e:
            flash(f"Error al intentar iniciar sesión: {str(e)}", 'danger')
            return None
    
    @staticmethod
    def register(username, email, password):
        try:
            user = AuthService.register(username, email, password)
            flash('Cuenta creada. Ahora ya puedes iniciar sesión!', 'success')
            return user
        except ValueError as e:
            flash('Este usuario ya existe', 'danger')  # Error: nombre de usuario o correo ya existen
        except Exception as e:
            flash(f"Un error ha ocurrido: {str(e)}", 'danger')  # Manejo de excepciones generales
        return None

    @staticmethod
    def logout():
        try:
            AuthService.logout()
            flash('Has cerrado sesión correctamente.', 'success')
        except Exception as e:
            flash(f"Un error ha ocurrido al cerrar sesión: {str(e)}", 'danger')
