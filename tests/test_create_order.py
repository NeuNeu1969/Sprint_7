import allure
import pytest

from api.orders_api import OrdersApi
from data import STATUS_CREATED, ORDER_DATA, ORDER_COLOR_CASES, ORDER_COLOR_IDS


class TestCreateOrder:

    @allure.feature("Заказ")
    @allure.story("Создание заказа")
    @allure.title("Заказ создаётся с любым вариантом цвета, в ответе есть track")
    @pytest.mark.parametrize("color_case", ORDER_COLOR_CASES, ids=ORDER_COLOR_IDS)
    def test_create_order_with_color_options(self, color_case):
        # Собирает заказ, общие данные и цвет
        payload = ORDER_DATA.copy()
        payload.update(color_case)
        response = OrdersApi().create_order(payload)

        # Проверяет код ответа и наличие track
        assert response.status_code == STATUS_CREATED
        assert "track" in response.json()

