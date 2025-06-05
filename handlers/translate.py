from aiogram import Router, types, F
from utils.translator import to_english

router = Router()

# Все текстовые сообщения, которые НЕ начинаются с '/'
@router.message(F.text & ~F.text.startswith("/"))
async def translate_any_text(message: types.Message):
    """Обрабатывает любой текст (не команду) — переводит на английский и отправляет ответом."""
    eng = await to_english(message.text)
    await message.reply(f"🇬🇧 {eng}")
