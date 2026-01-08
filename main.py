from config.settings import BOT_TOKEN

import asyncio
from aiogram import Bot, Dispatcher

from handlers import register_routes
from database.models import BaseModel
from database import engine


async def init_model():
    '''Initialize the BaseModel class'''
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)


async def main():
    '''
    Entry point for Telegram bot
    '''
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    register_routes(dp)

    await init_model()
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
