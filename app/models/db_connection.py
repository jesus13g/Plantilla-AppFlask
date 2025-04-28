from flask_sqlalchemy import SQLAlchemy

class Database:
    _instance = None
    db = SQLAlchemy()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def init_app(self, app):
        self.db.init_app(app)

    def get_session(self):
        return self.db.session

    def get_db(self):
        return self.db
