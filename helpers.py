import random
import string


def generate_random_string(length):
    # Случайные строки данных курьера
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_courier_data():
    # Логин, пароль и имя курьера
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10),
    }

