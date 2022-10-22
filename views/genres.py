# Импорт необходимых библиотек
from flask import request
from flask_restx import Resource, Namespace

# Импорт схемы Genre
from dao.model.genre import GenreSchema

# Импорт декораторов
from decorators.utils import auth_required, admin_required

# Импорт экземпляра класса GenreService
from implemented import genre_service

# Формирование нэймспейса
genre_ns = Namespace('genres')

# Формирование сереилизаторов для модели Genre для одного элемента и для списка
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        """
            Формирование представления для получения жанров
        """
        try:
            genres = genre_service.get_genres()
            return genres_schema.dump(genres), 200
        except Exception:
            return 404

    @admin_required
    def post(self):
        """
            Формирование представления для добавления нового жанра
        """
        try:
            data = request.json
            genre_service.create(data)
            return '', 201
        except Exception:
            return 404


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        """
            Формирование представления для получения жанра по id
        """
        try:
            genre = genre_service.get_genre(gid)
            return genre_schema.dump(genre), 200
        except Exception:
            return 404

    @admin_required
    def delete(self, gid):
        """
            Формирование представления для удалени жанра по id
        """
        try:
            genre_service.delete(gid)
            return '', 201
        except Exception:
            return  404

    @admin_required
    def put(self, gid):
        """
            Формирование представления для изменения данных жанра
        """
        try:
            data = request.json
            genre_service.update(data)
            return '', 201
        except Exception:
            return 404
