# Импорт библиотек Flask и Flask_restx
from flask import Flask
from flask_restx import Api

# Импорт конфигурации и базы данных
from config import Config
from setup_db import db

# Импорт нэймспейсов
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movies_ns
from views.users import user_ns
from views.authentification import auth_ns

def create_app(config_object):
    """
        Функция создания основного объекта app
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    """
        Функция подключения расширений
    """
    db.init_app(app)
    app.app_context().push()
    db.create_all()
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


if __name__ == '__main__':
    config = Config()
    app = create_app(Config())
    app.run(host="localhost", port=10002, debug=True)
