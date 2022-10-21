from config import Config

# Определение констант
algo = 'HS256'
PWD_HASH_SALT = b'secret here'
PWD_HASH_ITERATIONS = 100_000
secret = Config().SECRET_HERE

# "password": "admin_password",
# "username": "admin_name"