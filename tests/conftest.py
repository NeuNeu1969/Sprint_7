import pytest

from api.orders_api import OrdersApi
from data import ORDER_DATA
from api.courier_api import CourierApi
from data import STATUS_OK
from helpers import generate_courier_data


@pytest.fixture
def courier_data():
    # Создание / удаление курьера
    data = generate_courier_data()
    yield data
    courier_api = CourierApi()
    login_response = courier_api.login_courier({"login": data["login"], "password": data["password"]})
    if login_response.status_code == STATUS_OK:
        courier_api.delete_courier(login_response.json()["id"])


@pytest.fixture
def registered_courier(courier_data):
    # Передача данных о курьере в тесты
    courier_api = CourierApi()
    courier_api.create_courier(courier_data)
    login_response = courier_api.login_courier({"login": courier_data["login"], "password": courier_data["password"]})
    courier = {
        "login": courier_data["login"],
        "password": courier_data["password"],
        "firstName": courier_data["firstName"],
        "id": login_response.json()["id"],
    }
    return courier


@pytest.fixture
def created_order():
    orders_api = OrdersApi()
    # Создание заказа, сохранение номера
    track = orders_api.create_order(ORDER_DATA).json()["track"]
    # Получение id заказа по номеру
    order_id = orders_api.get_order_by_track(track).json()["order"]["id"]
    # Передача номера и id заказа в тест
    return {"track": track, "id": order_id}

