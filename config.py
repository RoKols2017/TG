import os
from dotenv import load_dotenv

load_dotenv()

TOKEN_TG = os.getenv("TOKEN_TG")
YANDEX_API_KEY = os.getenv("YANDEX_API_KEY")            # ключ для Яндекс.Погоды
YANDEX_GEOCODER_KEY = os.getenv("YANDEX_GEOCODER_KEY")  # необязательно, для Яндекс Геокодера
NOMINATIM_USER_AGENT = os.getenv("NOMINATIM_USER_AGENT", "weather-bot")

assert TOKEN_TG, "Set TOKEN_TG in .env"
assert YANDEX_API_KEY, "Set YANDEX_API_KEY in .env"