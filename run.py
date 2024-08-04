import logging
import asyncio
from aiogram import types, Dispatcher, Bot

from config import token
from app.handlers import router

async def main():
    bot = Bot(token="token")
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')