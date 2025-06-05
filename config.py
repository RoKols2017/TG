import os
from dotenv import load_dotenv

load_dotenv()

TOKEN_TG = os.getenv("TOKEN_TG")
YANDEX_API_KEY = os.getenv("YANDEX_API_KEY")            # ключ для Яндекс.Погоды
YANDEX_GEOCODER_KEY = os.getenv("YANDEX_GEOCODER_KEY")  # необязательно, для Яндекс Геокодера
NOMINATIM_USER_AGENT = os.getenv("NOMINATIM_USER_AGENT", "weather-bot")

DB_URL = os.getenv("DB_URL", "sqlite:///school_data.db")
DB_URL_PROD = os.getenv("DB_URL_PROD")

assert TOKEN_TG, "Set TOKEN_TG in .env"
assert YANDEX_API_KEY, "Set YANDEX_API_KEY in .env"

def get_database_url() -> str:
    """
    Возвращает строку подключения к БД в зависимости от режима.
    Если переменная окружения ENV=production, используется DB_URL_PROD (PostgreSQL), иначе DB_URL (SQLite).
    """
    env = os.getenv("ENV", "development")
    if env == "production":
        assert DB_URL_PROD, "Set DB_URL_PROD in .env for production"
        return DB_URL_PROD
    return DB_URL