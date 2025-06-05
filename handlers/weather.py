import re
from aiogram import Router, types
from aiogram.filters.command import Command
from utils.services import YandexWeatherService
from utils.formatters import format_weather

router = Router()
service = YandexWeatherService()

CITY_RE = re.compile(r"^/weather\s+(.+)", re.IGNORECASE | re.DOTALL)

@router.message(Command("weather"))
async def cmd_weather(message: types.Message):
    """Обрабатывает команду /weather — выводит погоду по указанному городу."""
    match = CITY_RE.match(message.text or "")
    if not match:
        await message.answer("⚠️ Укажите город: /weather Moscow")
        return

    city = match.group(1).strip()
    await message.chat.do("typing")

    weather_data = await service.get_weather(city)
    if weather_data is None:
        await message.answer("😔 Не удалось получить погоду. Попробуйте позже.")
    else:
        await message.answer(format_weather(city, weather_data))