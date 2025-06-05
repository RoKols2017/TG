import asyncio
import subprocess
import uuid
import os
from concurrent.futures import ThreadPoolExecutor
from gtts import gTTS

_executor = ThreadPoolExecutor()


def _generate_voice_sync(text: str, lang: str = "ru") -> str:
    """Блокирующая генерация .ogg-файла c помощью gTTS + ffmpeg CLI."""
    tmp = f"/tmp/{uuid.uuid4().hex}"
    mp3_path = f"{tmp}.mp3"
    ogg_path = f"{tmp}.ogg"

    gTTS(text=text, lang=lang).save(mp3_path)

    # ffmpeg -i input.mp3 -c:a libopus -b:a 48k output.ogg
    subprocess.run(
        [
            "ffmpeg", "-hide_banner", "-loglevel", "error",
            "-i", mp3_path,
            "-c:a", "libopus", "-b:a", "48k",
            ogg_path,
        ],
        check=True,
    )
    os.remove(mp3_path)
    return ogg_path


async def generate_voice(text: str, lang: str = "ru") -> str:
    """
    Асинхронно генерирует голосовой .ogg-файл из текста с помощью gTTS и ffmpeg.
    Возвращает путь к созданному .ogg-файлу.
    """
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(_executor, _generate_voice_sync, text, lang)
