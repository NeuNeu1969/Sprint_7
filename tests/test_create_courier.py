import allure
import pytest

from api.courier_api import CourierApi
from data import (
    STATUS_CREATED,
    STATUS_BAD_REQUEST,
    STATUS_CONFLICT,
    EXPECTED_OK_BODY,
    COURIER_REQUIRED_FIELDS,
    CREATE_COURIER_NOT_ENOUGH_DATA_MESSAGE,
    CREATE_COURIER_DUPLICATE_LOGIN_MESSAGE,
)
from helpers import generate_courier_data


class TestCreateCourier:

    @allure.feature("Курьер")
    @allure.story("Создание курьера")
    @allure.title("Курьера можно создать")
    def test_create_courier_success(self, courier_data):
        # Запрос на создание курьера
        response = CourierApi().create_courier(courier_data)

        # Проверка кода и ответа
        assert response.status_code == STATUS_CREATED
        assert response.json() == EXPECTED_OK_BODY

    @allure.feature("Курьер")
    @allure.story("Создание курьера")
    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_identical_courier_returns_conflict(self, courier_data):
        # Создаёт курьера, повторная отправка данных
        courier_api = CourierApi()
        courier_api.create_courier(courier_data)
        response = courier_api.create_courier(courier_data)

        # Проверка кода и ошибки
        assert response.status_code == STATUS_CONFLICT
        assert response.json()["message"] == CREATE_COURIER_DUPLICATE_LOGIN_MESSAGE

    @allure.feature("Курьер")
    @allure.story("Создание курьера")
    @allure.title("Нельзя создать курьера с существующим логином")
    def test_create_courier_with_existing_login_returns_conflict(self, courier_data):
        # Создаёт курьера, отправка других данных, логин тот же
        courier_api = CourierApi()
        courier_api.create_courier(courier_data)
        second_courier_data = generate_courier_data()
        second_courier_data["login"] = courier_data["login"]
        response = courier_api.create_courier(second_courier_data)

        # Проверка кода и ошибки
        assert response.status_code == STATUS_CONFLICT
        assert response.json()["message"] == CREATE_COURIER_DUPLICATE_LOGIN_MESSAGE

    @allure.feature("Курьер")
    @allure.story("Создание курьера")
    @allure.title("Без обязательного поля курьера создать нельзя")
    @pytest.mark.parametrize("missing_field", COURIER_REQUIRED_FIELDS)
    def test_create_courier_without_required_field_returns_error(self, courier_data, missing_field):
        # Удаляет обязательное поле и отправляет запрос
        payload = courier_data.copy()
        payload.pop(missing_field)
        response = CourierApi().create_courier(payload)

        # Проверка кода и ошибки
        assert response.status_code == STATUS_BAD_REQUEST
        assert response.json()["message"] == CREATE_COURIER_NOT_ENOUGH_DATA_MESSAGE

        