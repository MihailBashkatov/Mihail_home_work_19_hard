class DirectorService:
    def __init__(self, director_dao):
        self.director_dao = director_dao

    def get_directors(self):
        """
            Получение всех директоров
        """
        return self.director_dao.get_directors()

    def get_director(self, did):
        """
            Получение директора по id
        """
        return self.director_dao.get_director(did)

    def create_director(self, data):
        """
            Создание директора
        """
        return self.director_dao.create(data)

    def update_director(self, data):
        """
            Обновление директора
        """
        self.director_dao.update_director(data)
        return self.dao

    def delete_director(self, did):
        """
            Удаление директора
        """
        self.director_dao.delete(did)
