import uuid
import os
from concurrent.futures import ThreadPoolExecutor

from gtts import gTTS
from pydub import AudioSegment  # требует ffmpeg в системе

_executor = ThreadPoolExecutor()


def _generate_voice_sync(text: str, lang: str = "ru") -> str:
    """Блокирующая генерация .ogg-файла, возвращает путь."""
    mp3_path = f"/tmp/{uuid.uuid4().hex}.mp3"
    ogg_path = mp3_path.replace(".mp3", ".ogg")

    gTTS(text=text, lang=lang).save(mp3_path)

    # конвертируем в OGG/Opus
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(ogg_path, format="ogg", codec="libopus")
    os.remove(mp3_path)
    return ogg_path


async def generate_voice(text: str, lang: str = "ru") -> str:
    """Асинхронная оболочка."""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(_executor, _generate_voice_sync, text, lang)
