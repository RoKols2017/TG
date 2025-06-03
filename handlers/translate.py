from aiogram import Router, types
from utils.translator import to_english

router = Router()

@router.message(lambda m: m.text and not m.text.startswith("/"))
async def translate_any_text(message: types.Message):
    eng = to_english(message.text)
    await message.reply(f"🇬🇧 {eng}")
