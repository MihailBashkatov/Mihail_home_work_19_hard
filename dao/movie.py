from dao.model.movie import Movie


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_movies(self):
        """
            Получение всех фильмов
        """
        movies = self.session.query(Movie).all()
        return movies

    def get_movies_by_director_id(self, data):
        """
            Получение фильмов по директору
        """
        movies = self.session.query(Movie).filter(Movie.director_id == data)
        return movies

    def get_movies_by_genre_id(self, data):
        """
            Получение фильмов по жанру
        """
        movies = self.session.query(Movie).filter(Movie.genre_id == data)
        return movies

    def get_movies_by_year(self, data):
        """
            Получение фильмов по году
        """
        movies = self.session.query(Movie).filter(Movie.year == data)
        return movies

    def get_movie(self, mid):
        """
            Получение фильма по id
        """
        movie = self.session.query(Movie).filter(Movie.id == mid).one()
        return movie

    def create_movie(self, data):
        """
            Создание фильма
        """
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update_movie(self, data):
        """
            Обновление фильма
        """
        mid = data.get('id')
        self.session.query(Movie).filter(Movie.id == mid).update(data)
        self.session.commit()

    def delete_movie(self, mid):
        """
            Удаление фильма
        """
        movie = self.get_movie(mid)
        self.session.delete(movie)
        self.session.commit()
