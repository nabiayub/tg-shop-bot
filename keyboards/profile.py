from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def profile_menu_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Top Up',
                callback_data='deposit'
            )
        ]
    ])