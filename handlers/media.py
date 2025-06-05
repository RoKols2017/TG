import os
from datetime import datetime

from aiogram import Router, F, Bot
from aiogram.types import Message

router = Router()

IMG_DIR = "img"


@router.message(F.photo)
async def save_photo(message: Message, bot: Bot) -> None:
    """Обрабатывает получение фото — сохраняет самое большое фото в папку img/."""
    photo = message.photo[-1]                     # последнее = наибольшее
    file = await bot.get_file(photo.file_id)

    os.makedirs(IMG_DIR, exist_ok=True)
    ext = os.path.splitext(file.file_path)[1]     # .jpg / .jpeg / .png
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    local_path = os.path.join(
        IMG_DIR,
        f"{photo.file_unique_id}_{ts}{ext}",
    )

    await bot.download_file(file.file_path, destination=local_path)
    await message.answer("📸 Фото сохранено!")
