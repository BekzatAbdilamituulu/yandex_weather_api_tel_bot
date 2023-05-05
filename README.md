Заходим Кабинет разработчика яндекс https://developer.tech.yandex.ru/services/ Активируем ключ API.

url = "https://api.weather.yandex.ru/v2/informers?lat=55.75222&lon=37.61556"
lat=55.75222&lon=37.61556 - координаты местоположения

headers = {"X-Yandex-API-Key": "API ключ"} - поставим полученный ключ

В ответ получаем json ответ.