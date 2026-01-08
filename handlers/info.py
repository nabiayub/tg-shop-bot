from aiogram import Router, types, F

router = Router()

@router.message(F.text == 'About us')
async def info(message: types.Message):
    '''
    Hanlder for About us command.
    Describes what the bot is used for

    '''
    await message.answer('''
I am bot for buying books.
You can watch my catalog and buy the book you liked.

Good reading)
    ''')

