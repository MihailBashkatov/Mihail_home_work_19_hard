# Импорт необходимых библиотек
from marshmallow import Schema, fields

# Импорт базы данных
from setup_db import db

# Формирование класса User
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String)

# Формирование схемы User
class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()