import os
from datetime import datetime

from aiogram import Router, types, Bot
from aiogram.types import ContentType

router = Router()

IMG_DIR = "img"


@router.message(ContentType.PHOTO)
async def save_photo(message: types.Message, bot: Bot):
    """Скачивает последнюю (наибольшего размера) фотографию из сообщения."""
    photo = message.photo[-1]                      # самое большое превью
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    ext = os.path.splitext(file_path)[1]           # .jpg, .png…

    os.makedirs(IMG_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    local_path = os.path.join(IMG_DIR, f"{photo.file_unique_id}_{ts}{ext}")

    await bot.download_file(file_path, destination=local_path)
    await message.answer("📸 Фото сохранено!")
