# Коды ответов
STATUS_OK = 200
STATUS_CREATED = 201
STATUS_BAD_REQUEST = 400
STATUS_NOT_FOUND = 404
STATUS_CONFLICT = 409

# Тело успешного ответа
EXPECTED_OK_BODY = {"ok": True}

# Тексты ошибок
CREATE_COURIER_NOT_ENOUGH_DATA_MESSAGE = "Недостаточно данных для создания учетной записи"
CREATE_COURIER_DUPLICATE_LOGIN_MESSAGE = "Этот логин уже используется. Попробуйте другой."
LOGIN_NOT_ENOUGH_DATA_MESSAGE = "Недостаточно данных для входа"
LOGIN_ACCOUNT_NOT_FOUND_MESSAGE = "Учетная запись не найдена"

# Поля курьера, без них создание не проходит
COURIER_REQUIRED_FIELDS = ["login", "password"]

# Искажённое поле, неверные данные для входа
WRONG_CREDENTIAL_FIELDS = ["login", "password"]

# Причина, когда логин помечен xfail
LOGIN_WITHOUT_PASSWORD_BUG_REASON = "Баг стенда: логин без поля password не возвращает ответ (ReadTimeout), ожидается 400"

# Тело заказа без цвета
ORDER_DATA = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-12-01",
    "comment": "Saske, come back to Konoha",
}

# Параметризация цветов: один цвет, другой, оба, без цвета
ORDER_COLOR_CASES = [
    {"color": ["BLACK"]},
    {"color": ["GREY"]},
    {"color": ["BLACK", "GREY"]},
    {},
]
ORDER_COLOR_IDS = ["black", "grey", "black_and_grey", "no_color"]

# Сообщение, удаление, несуществующий id
DELETE_COURIER_NOT_FOUND_MESSAGE = "Курьера с таким id нет."
# Сообщение, приём заказа без нужного параметра
ACCEPT_ORDER_NOT_ENOUGH_DATA_MESSAGE = "Недостаточно данных для поиска"

