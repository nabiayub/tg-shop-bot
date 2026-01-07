from aiogram import Router, types, F

router = Router()

@router.message(F.text == 'About us')
async def info(message: types.Message):
    await message.answer('''
I am bot for buying books.
You can watch my catalog and buy the book you liked.

Good reading)
    ''')

