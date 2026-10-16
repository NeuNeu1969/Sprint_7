import allure
import requests
from constants import REQUEST_TIMEOUT
from urls import BASE_URL


class BaseApi:
    @allure.step("Отправить запрос к API")
    def send_request(self, method, path, json_body=None, params=None):
        # Две попытки перехвата обрыва
        for attempt in range(2):
            try:
                # Отправка запроса
                return requests.request(
                    method,
                    BASE_URL + path,
                    json=json_body,
                    params=params,
                    timeout=REQUEST_TIMEOUT,
                )
            except requests.exceptions.ConnectionError:
                # Обрыв, следующая попытка
                continue
        # Заключительная попытка
        return requests.request(
            method,
            BASE_URL + path,
            json=json_body,
            params=params,
            timeout=REQUEST_TIMEOUT,
        )

    