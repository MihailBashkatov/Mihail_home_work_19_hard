# Импорт необходимых библиотек
from flask import request, abort
from flask_restx import Namespace, Resource

# Импорт экземпляра класса AuthentificationService
from implemented import authentification_service

# Формирование нэймспейса
auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        """
            Аутентификация и авторизация пользователя по username and password
        """
        data = request.json
        user_name = data.get('username', None)
        password = data.get('password', None)

        if None in [user_name, password]:
            abort(401)

        # Получение токенов
        tokens = authentification_service.generate_tokens(user_name, password)
        return tokens

    def put(self):
        """
            Обновление refresh_token
        """
        request_json = request.json
        refresh_token = request_json.get("refresh_token")
        tokens = authentification_service.update_tokens(refresh_token)
        return tokens
