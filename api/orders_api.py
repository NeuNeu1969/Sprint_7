import allure

from api.base_api import BaseApi
from urls import ORDERS_ENDPOINT, ORDERS_ACCEPT_ENDPOINT, ORDERS_TRACK_ENDPOINT


class OrdersApi(BaseApi):

    @allure.step("Создать заказ")
    def create_order(self, payload):
        #Запрос на создание заказа
        return self.send_request("POST", ORDERS_ENDPOINT, json_body=payload)

    @allure.step("Получить список заказов")
    def get_orders_list(self):
        # Запрос на получение списка заказов
        return self.send_request("GET", ORDERS_ENDPOINT)

    @allure.step("Получить заказ по номеру track")
    def get_order_by_track(self, track):
        # Получение id заказа, чтобы принять
        return self.send_request("GET", ORDERS_TRACK_ENDPOINT, params={"t": track})

    @allure.step("Принять заказ")
    def accept_order(self, order_id, courier_id):
        # Принять заказ по id заказа и id курьера
        return self.send_request(
            "PUT",
            ORDERS_ACCEPT_ENDPOINT + "/" + str(order_id),
            params={"courierId": courier_id},
        )

    