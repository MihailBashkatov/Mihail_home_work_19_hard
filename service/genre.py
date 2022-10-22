from dao.genre import GenreDAO


class GenreService:
    def __init__(self, genre_dao):
        self.genre_dao = genre_dao

    def get_genres(self):
        """
            Получение всех жанров
        """
        return self.genre_dao.get_genres()

    def get_genre(self, gid):
        """
            Получение жанра по id
        """
        return self.genre_dao.get_genre(gid)

    def create_genre(self, data):
        """
            Создание жанра
        """
        return self.genre_dao.create(data)

    def update_genre(self, data):
        """
            Обновление жанра
        """
        self.genre_dao.update(data)
        return self.dao

    def delete_genre(self, gid):
        """
            Удаление жанра
        """
        self.genre_dao.delete(gid)
