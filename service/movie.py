class MovieService:

    def __init__(self, movie_dao):
        self.movie_dao = movie_dao

    def get_movies(self, param, data):
        """
            Формирование запроса в зависимости от параметров поиска
        """
        movies = self.movie_dao.get_movies()
        if param == 'director_id':
            movies = self.movie_dao.get_movies_by_director_id(data)
        if param == 'genre_id':
            movies = self.movie_dao.get_movies_by_genre_id(data)
        if param == 'year':
            movies = self.movie_dao.get_movies_by_year(data)
        return movies

    def get_movie(self, mid):
        """
            Получение фильма по id
        """
        return self.movie_dao.get_movie(mid)

    def create_movie(self, data):
        """
            Создание фильма
        """
        return self.movie_dao.create_movie(data)

    def update_movie(self, data):
        """
            Обновление фильма по id
        """
        return self.movie_dao.update_movie(data)

    def delete_movie(self, mid):
        """
            Удаление фильма по id
        """
        self.movie_dao.delete_movie(mid)
