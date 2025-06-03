import aiohttp
import logging
from typing import Optional, Dict, Any

from config import (
    YANDEX_API_KEY,
    YANDEX_GEOCODER_KEY,
    NOMINATIM_USER_AGENT,
)

logger = logging.getLogger(__name__)

class YandexWeatherService:
    """Получение координат через Яндекс‑Геокодер (если доступен)
    с автоматическим резервом на Nominatim (OpenStreetMap)."""

    YANDEX_GEO_URL = "https://geocode-maps.yandex.ru/1.x"
    NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
    WEATHER_URL = "https://api.weather.yandex.ru/v2/informers"

    async def _fetch_json(
        self,
        url: str,
        *,
        headers: dict | None = None,
        params: dict | None = None,
    ) -> Optional[Dict[str, Any]]:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url, params=params, timeout=10) as resp:
                if resp.status == 200:
                    return await resp.json()
                logger.error("HTTP %s for %s", resp.status, url)
                return None

    async def _geocode_yandex(self, city: str) -> Optional[Dict[str, float]]:
        """Пытаемся получить координаты через Яндекс‑Геокодер."""
        if not YANDEX_GEOCODER_KEY:
            return None
        params = {
            "geocode": city,
            "format": "json",
            "apikey": YANDEX_GEOCODER_KEY,
            "lang": "ru_RU",
        }
        data = await self._fetch_json(self.YANDEX_GEO_URL, params=params)
        try:
            pos = (
                data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
            )
            lon, lat = map(float, pos.split())
            return {"lat": lat, "lon": lon}
        except Exception:
            logger.exception("Yandex geocoder parse failed")
            return None

    async def _geocode_nominatim(self, city: str) -> Optional[Dict[str, float]]:
        """OpenStreetMap Nominatim (без ключа, но нужен User‑Agent)."""
        headers = {"User-Agent": NOMINATIM_USER_AGENT}
        params = {"q": city, "format": "json", "limit": 1}
        data = await self._fetch_json(self.NOMINATIM_URL, headers=headers, params=params)
        try:
            first = data[0]
            return {"lat": float(first["lat"]), "lon": float(first["lon"])}
        except Exception:
            logger.exception("Nominatim geocoder parse failed")
            return None

    async def _geocode(self, city: str) -> Optional[Dict[str, float]]:
        # Сначала пробуем Яндекс‑Геокодер (если есть ключ), затем Nominatim
        coords = await self._geocode_yandex(city)
        if coords:
            return coords
        return await self._geocode_nominatim(city)

    async def get_weather(self, city: str) -> Optional[Dict[str, Any]]:
        coords = await self._geocode(city)
        if not coords:
            return None

        headers = {"X-Yandex-API-Key": YANDEX_API_KEY}
        params = {
            "lat": coords["lat"],
            "lon": coords["lon"],
            "lang": "ru_RU",
        }
        return await self._fetch_json(self.WEATHER_URL, headers=headers, params=params)