from aiogram import Router, types
from aiogram.filters.command import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    """Обрабатывает команду /start — приветствие пользователя."""
    await message.answer("👋 Привет! Используй /help, чтобы узнать доступные команды.")

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    """Обрабатывает команду /help — выводит справку по возможностям бота."""
    help_text = (
        "<b>Доступные команды и функции</b>\n\n"
        "/start — приветствие\n"
        "/help — эта справка\n"
        "/weather <город> — текущая погода\n"
        "/voice <текст> — отправлю голосовое с озвучкой текста\n"
        "/add_student — добавить нового ученика (имя, возраст, класс, город)\n\n"
        "🖼 Если пришлёшь фото — сохраню его в папке <code>img/</code>.\n"
        "🇬🇧 Любой обычный текст я автоматически переведу на английский и пришлю ответом."
    )
    await message.answer(help_text)
