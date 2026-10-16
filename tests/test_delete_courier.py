import allure
from api.courier_api import CourierApi
from data import (
    STATUS_OK,
    STATUS_NOT_FOUND,
    EXPECTED_OK_BODY,
    DELETE_COURIER_NOT_FOUND_MESSAGE,
)


@allure.feature("Курьер")
@allure.story("Удаление курьера")
class TestDeleteCourier:

    @allure.title("Удаление курьера возвращает 200 и ok: true")
    def test_delete_courier_success(self, registered_courier):
        courier_api = CourierApi()
        # Удаление курьера по id
        response = courier_api.delete_courier(registered_courier["id"])
        # Проверка кода
        assert response.status_code == STATUS_OK
        # Проверка тела
        assert response.json() == EXPECTED_OK_BODY

    @allure.title("Удаление курьера с несуществующим id возвращает 404 и сообщение")
    def test_delete_nonexistent_courier_returns_error(self, registered_courier):
        courier_api = CourierApi()
        # Удаление курьера
        courier_api.delete_courier(registered_courier["id"])
        # Повторное удаление
        response = courier_api.delete_courier(registered_courier["id"])
        # Проверка кода
        assert response.status_code == STATUS_NOT_FOUND
        # Проверка текста ошибки
        assert response.json()["message"] == DELETE_COURIER_NOT_FOUND_MESSAGE

