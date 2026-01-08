
from aiogram import Router, types
from aiogram.filters import Command

from keyboards.menu import main_menu_kb
from repositories.user import UserRepo

router = Router()

@router.message(Command('start'))
async def start_bot(message: types.Message, user_repo: UserRepo):
    """
    Handler for /start command.
    Greets the user and shows the main menu keyboard.
    """

    await user_repo.create_or_update_user(
        tg_id=message.from_user.id,
        username=message.from_user.username,
        fullname=message.from_user.full_name
    )

    await message.answer(
        f'''
Hello {message.from_user.full_name}!
I'm a book shop. Choose menu below:''',
        reply_markup=main_menu_kb(),

    )