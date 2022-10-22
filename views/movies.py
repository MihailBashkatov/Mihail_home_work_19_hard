# Импорт необходимых библиотек
from flask import request
from flask_restx import Resource, Namespace

# Импорт схемы Movie
from dao.model.movie import MovieSchema

# Импорт декораторов
from decorators.utils import auth_required, admin_required

# Импорт экземпляра класса MovieService
from implemented import movie_service

# Формирование нэймспейса
movies_ns = Namespace('movies')

# Формирование сереилизаторов для модели Movie для одного элемента и для списка
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        """
            Формирование представления для получения фильмов
        """
        try:
            param = None
            data = None
            data_by_director_id = request.args.get('director_id')
            data_by_genre_id = request.args.get('genre_id')
            data_by_year = request.args.get('year')

            # При квери-запросе по director
            if data_by_director_id:
                param = "director_id"
                data = data_by_director_id

            # При квери-запросе по genre
            if data_by_genre_id:
                param = "genre_id"
                data = data_by_genre_id

            # При квери-запросе по year
            if data_by_year:
                param = "year"
                data = data_by_year
            movies = movie_service.get_movies(param, data)
            movies_list = movies_schema.dump(movies)

            # Если запрос возвращает пустой список, то возвращается 'No such movie'
            if len(movies_list) == 0:
                return 'No such movie', 200
            print(request.headers)
            return movies_list, 200
        except Exception:
            return 404

    @admin_required
    def post(self):
        """
            Формирование представления для добавления нового фильма
        """
        try:
            data = request.json
            movie_service.create_movie(data)
            return '', 201
        except Exception:
            return 404


@movies_ns.route('/<mid>')
class MovieView(Resource):
    @auth_required
    def get(self, mid):
        """
            Формирование представления для получения фильма по id
            В случае отсутствия фильма возвращается 'No such movie'
        """
        try:
            movie = movie_service.get_movie(mid)
            if movie_schema.dump(movie) == {}:
                return 'No such movie', 200
            return movie_schema.dump(movie), 200
        except Exception:
            return 404

    @admin_required
    def put(self, mid):
        try:
            """
                Формирование представления для изменения данных режиссера по id
                В случае отсутствия режиссера - ошибка
            """
            data = request.json
            movie_service.update_movie(data, mid)
            return '', 201
        except Exception:
            return 404

    @admin_required
    def delete(self, mid):
        """
            Формирование представления для удалени режиссера по id
            В случае отсутствия режиссера - ошибка
        """
        try:
            movie_service.delete_movie(mid)
            return '', 201
        except Exception:
            return 404
