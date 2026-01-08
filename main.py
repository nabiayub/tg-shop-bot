from config.settings import BOT_TOKEN

import asyncio
from aiogram import Bot, Dispatcher

from handlers import register_routes


async def main():
    '''
    Entry point for Telegram bot
    '''
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    register_routes(dp)

    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")