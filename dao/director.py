from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_directors(self):
        """
            Получение всех директоров
        """
        return self.session.query(Director).all()

    def get_director(self, did):
        """
            Получение диерктора по id
        """
        return self.session.query(Director).filter(Director.id == did).one()

    def create(self, data):
        """
            Создание директора
        """
        director_created = Director(**data)
        self.session.add(director_created)
        self.session.commit()
        return director_created

    def delete(self, did):
        """
            Удаление директора
        """
        director = self.get_director(did)
        self.session.delete(director)
        self.session.commit()

    def update(self, data):
        """
            Обновление директора
        """
        did = data.get('id')
        self.session.query(Director).filter(Director.id == did).update(data)
        self.session.commit()
