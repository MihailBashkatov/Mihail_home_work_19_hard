# Импорт необходимых библиотек
from flask import request
from flask_restx import Namespace, Resource

# Импорт схемы User
from dao.model.user import UserSchema

# Импорт декораторов
from decorators.utils import admin_required, auth_required

# Импорт экземпляра класса UserService
from implemented import user_service

# Формирование нэймспейса
user_ns = Namespace('users')

# Формирование сереилизаторов для модели User для одного элемента и для списка
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/<username>')
class UserView(Resource):
    @admin_required
    def get(self, username):
        """
            Формирование представления для получения пользователя по имени
        """
        try:
            user = user_service.get_user(username)
            return user_schema.dump(user), 200
        except Exception:
            return "No such user", 404

    @admin_required
    def delete(self, username):
        """
            Формирование представления для удалени пользователя по имени
        """
        try:
            user_service.delete_user(username)
            return '', 200
        except Exception:
            return 404

    @auth_required
    def put(self, username):
        """
            Формирование представления для изменения данных пользователя
        """
        try:
            data = request.json
            print(data)
            user_service.update_user(data)
            return '', 201
        except Exception:
            return 404


@user_ns.route('/')
class UsersView(Resource):
    def post(self):
        """
            Формирование представления для добавления нового пользователя
        """
        try:
            data = request.json
            user_service.create_user(data)
            return '', 201
        except Exception:
            return 404

    @admin_required
    def get(self):
        """
            Формирование представления для получения пользователей
        """
        try:
            users = user_service.get_all()
            return users_schema.dump(users)
        except Exception:
            return 404
