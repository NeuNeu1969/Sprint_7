import allure
from api.orders_api import OrdersApi
from data import (
    STATUS_OK,
    STATUS_NOT_FOUND,
    STATUS_BAD_REQUEST,
    EXPECTED_OK_BODY,
    ACCEPT_ORDER_NOT_ENOUGH_DATA_MESSAGE,
)


@allure.feature("Заказ")
@allure.story("Принятие заказа")
class TestAcceptOrder:

    @allure.title("Принятие заказа возвращает 200 и ok: true")
    def test_accept_order_success(self, registered_courier, created_order):
        orders_api = OrdersApi()
        # Принятие заказа курьером
        response = orders_api.accept_order(created_order["id"], registered_courier["id"])
        # Проверка кода
        assert response.status_code == STATUS_OK
        # Проверка тела
        assert response.json() == EXPECTED_OK_BODY

    @allure.title("Принятие заказа без id возвращает 400 и ошибку")
    def test_accept_order_error(self, created_order):
        orders_api = OrdersApi()
        # Принятие заказа без id курьера
        response = orders_api.accept_order(created_order["id"], None)
        # Проверка кода
        assert response.status_code == STATUS_BAD_REQUEST
        # Проверка текста ошибки
        assert response.json()["message"] == ACCEPT_ORDER_NOT_ENOUGH_DATA_MESSAGE

