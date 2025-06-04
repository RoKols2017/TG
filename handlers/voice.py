import os
from aiogram import Router, types
from aiogram.filters.command import Command, CommandObject
from aiogram.types import FSInputFile        # ← добавили
from utils.voice import generate_voice

router = Router()


@router.message(Command("voice"))
async def cmd_voice(message: types.Message, command: CommandObject):
    text = command.args
    if not text:
        await message.answer("⚠️ Использование: /voice <текст>")
        return

    await message.chat.do("record_voice")

    ogg_path = await generate_voice(text, lang="ru")
    try:
        voice = FSInputFile(ogg_path)        # оборачиваем путь в InputFile
        await message.answer_voice(voice)
    finally:
        os.remove(ogg_path)
