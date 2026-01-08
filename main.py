from config.settings import BOT_TOKEN, DATABASE_URL

import asyncio
from aiogram import Bot, Dispatcher

from handlers import register_routes
from database.models import BaseModel
from middlewares import register_middlewares
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker



async def init_model(engine):
    '''Initialize the BaseModel class'''
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)


async def main():
    '''
    Entry point for Telegram bot
    '''
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    engine = create_async_engine(
        url=DATABASE_URL,

    )
    session_maker = async_sessionmaker(engine, expire_on_commit=False)

    register_middlewares(dp, session_maker)
    register_routes(dp)

    await init_model(engine)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
