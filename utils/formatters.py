def format_weather(city: str, data: dict) -> str:
    """Форматировать данные фактической погоды Яндекс‑API."""
    fact = data.get("fact", {})
    temp = fact.get("temp")
    feels_like = fact.get("feels_like")
    condition = fact.get("condition")
    humidity = fact.get("humidity")
    wind_speed = fact.get("wind_speed")
    pressure = fact.get("pressure_mm")

    # Человеческие описания + emoji
    condition_map = {
        "clear": ("ясно", "☀️"),
        "partly-cloudy": ("малооблачно", "🌤"),
        "cloudy": ("облачно с прояснениями", "⛅️"),
        "overcast": ("пасмурно", "☁️"),
        "light-rain": ("небольшой дождь", "🌦"),
        "rain": ("дождь", "🌧"),
        "heavy-rain": ("сильный дождь", "🌧"),
        "showers": ("ливень", "🌧"),
        "snow": ("снег", "🌨"),
        "light-snow": ("небольшой снег", "🌨"),
        "heavy-snow": ("сильный снег", "❄️"),
        "sleet": ("дождь со снегом", "🌨"),
        "hail": ("град", "🌨"),
        "thunderstorm": ("гроза", "⛈"),
        "thunderstorm-with-rain": ("гроза с дождём", "⛈"),
        "thunderstorm-with-hail": ("гроза с градом", "⛈"),
    }
    state_text, emoji = condition_map.get(condition, (condition or "—", "🌡"))

    return (
        f"{emoji} Погода в {city.title()}:\n"
        f"Температура: {temp} °C (ощущается как {feels_like} °C)\n"
        f"Состояние: {state_text}\n"
        f"Влажность: {humidity} %\n"
        f"Ветер: {wind_speed} м/с\n"
        f"Давление: {pressure} мм рт. ст."
    )