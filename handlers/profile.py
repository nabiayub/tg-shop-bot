from aiogram import F, Router, types
from aiogram.enums import ParseMode

from database import User
from keyboards import profile as profile_kb
from repositories.user import UserRepo

router = Router()


@router.message(F.text == 'Profile')
async def user_profile_info(
        message: types.Message,
        user_repo: UserRepo):

    user: User = await user_repo.get_user_by_tg_id(message.from_user.id)

    await message.answer(
        f'<b>{message.from_user.full_name}</b>\n\n'
        f'Username: {user.username or ''}\n'
        f'ID: <code>{user.tg_id}</code>\n'
        f'Balance: {user.get_balance} dollars\n',
        parse_mode=ParseMode.HTML,
        reply_markup=profile_kb.profile_menu_kb()
    )
