import aiohttp
from urllib.parse import quote_plus


async def to_english(text: str) -> str:
    """
    Перевод любого текста → English с помощью
    https://translate.googleapis.com/translate_a/single (не требует ключа).

    • sl=auto  — авто-определение входного языка
    • tl=en    — перевод на английский

    Возвращает переведённую строку или исходную, если API недоступно.
    """
    url = (
        "https://translate.googleapis.com/translate_a/single"
        "?client=gtx&sl=auto&tl=en&dt=t&q=" + quote_plus(text)
    )

    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=5) as resp:
            if resp.status != 200:
                return text  # fallback: отдать оригинал
            data = await resp.json()

    # data[0] — список сегментов; каждый сегмент = [перевод, оригинал, ...]
    translated = "".join(seg[0] for seg in data[0] if seg[0])
    return translated.strip() or text
