from traceback import print_tb

from aiogram import Router, types
from aiogram.filters import Command
from sqlalchemy import text

from keyboards.menu import main_menu_kb

router = Router()

@router.message(Command('start'))
async def start_bot(message: types.Message, session):
    '''
    Handler for /start command.
    Greets the user and shows the main menu keyboard.
    '''


    await message.answer(
        f'''
Hello {message.from_user.full_name}!
I'm a book shop. Choose menu below:''',
        reply_markup=main_menu_kb(),

    )