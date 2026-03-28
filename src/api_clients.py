import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_mock_bank_data() -> dict:
    """
    Возвращает заглушку данных о банковском счете (баланс и процентная ставка).
    Используется временно, так как у банка нет открытого API для физлиц.
    """
    return {"balance": 250000.0, "rate": 13.5}


def get_exchanges_rate() -> dict:
    """Получает актуальные курсы валют (USD, EUR)"""

    url = os.getenv("EXCHANGE_CB_URL")

    if url is None:
        raise ValueError("НЕ ЗАДАН EXCHANGE_CB_URL! ВНЕСИТЕ НУЖНУЮ ССЫЛКУ В .env-файл")

    response = requests.get(url)
    data = response.json()
    usd_rate = data["Valute"]["USD"]["Value"]
    eur_rate = data["Valute"]["EUR"]["Value"]
    return {"USD": usd_rate, "EUR": eur_rate}
