import allure

from api.base_api import BaseApi
from urls import COURIER_ENDPOINT, COURIER_LOGIN_ENDPOINT


class CourierApi(BaseApi):

    @allure.step("Создать курьера")
    def create_courier(self, payload):
        # Создание курьера
        return self.send_request("POST", COURIER_ENDPOINT, json_body=payload)

    @allure.step("Авторизовать курьера")
    def login_courier(self, payload):
        # Авторизация курьера
        return self.send_request("POST", COURIER_LOGIN_ENDPOINT, json_body=payload)

    @allure.step("Удалить курьера")
    def delete_courier(self, courier_id):
        # Удаление записи о курьере в БД
        return self.send_request("DELETE", COURIER_ENDPOINT + "/" + str(courier_id))

    