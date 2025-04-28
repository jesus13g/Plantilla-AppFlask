from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, login_required, current_user
from .auth.authController import AuthController
from .models.tables import User
from .models.db_connection import Database

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    # Inicialización de la base de datos y LoginManager
    db_instance = Database()
    db_instance.init_app(app)

    login_manager = LoginManager(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route('/')
    def home():
        return render_template('main.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = AuthController.login(username, password)
            if user:
                login_user(user)
                return redirect(url_for('dashboard'))
        return render_template('login.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            user = AuthController.register(username, email, password)
            if user:
                return redirect(url_for('login'))
        return render_template('register.html')

    @app.route('/logout')
    def logout():
        AuthController.logout()
        return redirect(url_for('home'))
    

    @app.route('/dashboard')
    @login_required
    def dashboard():
        return render_template('dashboard.html')


    return app
