from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_genre(self, gid):
        """
            Получение жанра по id
        """
        return self.session.query(Genre).filter(Genre.id == gid).one()

    def get_genres(self):
        """
            Получение всех жанров
        """
        return self.session.query(Genre).all()

    def create(self, data):
        """
            Создание жанра
        """
        genre_created = Genre(**data)
        self.session.add(genre_created)
        self.session.commit()
        return genre_created

    def delete(self, gid):
        """
            Удаление жанра
        """
        genre = self.get_genre(gid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, data):
        """
            Обновление жанра
        """
        gid = data.get('id')
        self.session.query(Genre).filter(Genre.id == gid).update(data)
        self.session.commit()
