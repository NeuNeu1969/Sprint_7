import allure

from api.orders_api import OrdersApi
from data import STATUS_OK


class TestOrdersList:

    @allure.feature("Заказ")
    @allure.story("Список заказов")
    @allure.title("В теле ответа возвращается список заказов")
    def test_get_orders_list_returns_list(self):
        # Запрос списка заказов
        response = OrdersApi().get_orders_list()

        # Проверка кода и содержимого поля orders
        assert response.status_code == STATUS_OK
        assert isinstance(response.json()["orders"], list)

        