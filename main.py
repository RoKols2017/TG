import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import TOKEN_TG
from handlers import common, weather

logging.basicConfig(level=logging.INFO)

async def main() -> None:
    bot = Bot(token=TOKEN_TG)
    dp = Dispatcher(storage=MemoryStorage())

    # Register routers
    dp.include_router(common.router)
    dp.include_router(weather.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())