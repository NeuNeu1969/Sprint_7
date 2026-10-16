import allure
import pytest

from api.courier_api import CourierApi
from data import (
    STATUS_OK,
    STATUS_BAD_REQUEST,
    STATUS_NOT_FOUND,
    WRONG_CREDENTIAL_FIELDS,
    LOGIN_NOT_ENOUGH_DATA_MESSAGE,
    LOGIN_ACCOUNT_NOT_FOUND_MESSAGE,
    LOGIN_WITHOUT_PASSWORD_BUG_REASON,
)
from helpers import generate_random_string, generate_courier_data


class TestLoginCourier:

    @allure.feature("Курьер")
    @allure.story("Логин курьера")
    @allure.title("Курьер может авторизоваться, в ответе возвращается id")
    def test_login_courier_success(self, registered_courier):
        # Авторизация с логином и паролем созданного курьера
        payload = {"login": registered_courier["login"], "password": registered_courier["password"]}
        response = CourierApi().login_courier(payload)

        # Проверка кода ответа наличия id курьера
        assert response.status_code == STATUS_OK
        assert response.json()["id"] == registered_courier["id"]

    @allure.feature("Курьер")
    @allure.story("Логин курьера")
    @allure.title("Без логина авторизоваться нельзя")
    def test_login_without_login_returns_error(self, registered_courier):
        # Отправка запроса без поля login
        payload = {"password": registered_courier["password"]}
        response = CourierApi().login_courier(payload)

        # Проверка кода и сообщения об ошибке
        assert response.status_code == STATUS_BAD_REQUEST
        assert response.json()["message"] == LOGIN_NOT_ENOUGH_DATA_MESSAGE

    @allure.feature("Курьер")
    @allure.story("Логин курьера")
    @allure.title("Без пароля авторизоваться нельзя")
    @pytest.mark.xfail(reason=LOGIN_WITHOUT_PASSWORD_BUG_REASON)
    def test_login_without_password_returns_error(self, registered_courier):
        # Запрос без поля password
        payload = {"login": registered_courier["login"]}
        response = CourierApi().login_courier(payload)

        # Проверка кода и сообщения об ошибке
        assert response.status_code == STATUS_BAD_REQUEST
        assert response.json()["message"] == LOGIN_NOT_ENOUGH_DATA_MESSAGE

    @allure.feature("Курьер")
    @allure.story("Логин курьера")
    @allure.title("Неверный логин или пароль — ошибка")
    @pytest.mark.parametrize("wrong_field", WRONG_CREDENTIAL_FIELDS)
    def test_login_with_wrong_credential_returns_not_found(self, registered_courier, wrong_field):
        # Верные данные курьера с искажением поля
        payload = {"login": registered_courier["login"], "password": registered_courier["password"]}
        payload[wrong_field] = generate_random_string(10)
        response = CourierApi().login_courier(payload)

        # Проверка кода и сообщения об ошибке
        assert response.status_code == STATUS_NOT_FOUND
        assert response.json()["message"] == LOGIN_ACCOUNT_NOT_FOUND_MESSAGE

    @allure.feature("Курьер")
    @allure.story("Логин курьера")
    @allure.title("Несуществующий пользователь не может авторизоваться")
    def test_login_nonexistent_courier_returns_not_found(self):
        # Не зарегистрированные логин и пароль курьера
        courier = generate_courier_data()
        payload = {"login": courier["login"], "password": courier["password"]}
        response = CourierApi().login_courier(payload)

        # Проверка кода и сообщения об ошибке
        assert response.status_code == STATUS_NOT_FOUND
        assert response.json()["message"] == LOGIN_ACCOUNT_NOT_FOUND_MESSAGE

