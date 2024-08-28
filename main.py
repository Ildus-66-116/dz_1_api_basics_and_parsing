"""Сценарий Foursquare
Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию (например, кофейни, музеи, парки и т.д.).
Используйте API Foursquare для поиска заведений в указанной категории.
Получите название заведения, его адрес и рейтинг для каждого из них.
Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль."""

import os
import requests
from dotenv import load_dotenv
import json
from bs4 import BeautifulSoup

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

url = "https://api.foursquare.com/v3/places/search"

headers = {
    "accept": "application/json",
    "Authorization": os.getenv("API_KEY")
}

response = requests.get(url, headers=headers)
with open('foursquare.json', 'w') as f:
    json.dump(response.json(), f)

dict_foursquare = response.json()

request = input('Введите запрос: ')
for key, value in dict_foursquare.items():
    if key == request:
        print(key, value)
    elif value == request:
        print(key, value)
    else:
        print(f'Значение {request} не найден.')
