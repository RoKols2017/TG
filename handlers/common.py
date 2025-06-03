from aiogram import Router, types
from aiogram.filters.command import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("👋 Привет! Используй /help, чтобы узнать доступные команды.")

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = (
        "<b>Доступные команды</b>\n"
        "/start — приветствие\n"
        "/help — справка\n"
        "/weather &lt;город&gt; — погода в городе\n"
    )
    await message.answer(help_text)
    