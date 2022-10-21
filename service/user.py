# Импорт библиотек
import base64
import hashlib
import hmac

# Импорт констант
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao):
        self.dao = dao

    def get_user(self, user_name):
        """
            Получение пользователя по имени
        """
        return self.dao.get_user(user_name)

    def delete_user(self, user_name):
        """
            Удаление пользователя по имени
        """
        self.dao.delete_user(user_name)

    def create_user(self, data):
        """
            Создание пользователя
        """
        password = data.get('password')
        hashed_password = self.get_hash(password)
        data['password'] = hashed_password
        self.dao.create_user(data)

    def update_user(self, data):
        """
            Обновление пользователя
        """
        password = data.get('password')
        hashed_password = self.get_hash(password)
        data['password'] = hashed_password
        self.dao.update_user(data)

    def get_all(self):
        """
            Получение всех пользователей
        """
        return self.dao.get_all()

    def get_hash(self, password):
        """
            Хэширование пароля
        """
        hashed_password = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
            )
        return base64.b64encode(hashed_password)

    def compare_passwords(self, user_password, password):
        """
            Сравнение хэшированного пароля и введенного пароля
        """

        hashed_pasword = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
            )

        decoded_password = base64.b64decode(user_password)

        return hmac.compare_digest(decoded_password, hashed_pasword)
