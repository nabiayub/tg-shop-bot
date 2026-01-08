from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_kb() -> ReplyKeyboardMarkup:
    '''
    Generate a reply keyboard for the menu with following buttons:
    - Catalog
    - Profile
    - About US

    :return:
        ReplyKeyboardMarkup: Reply keyboard with menu buttons
    '''

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Catalog")],
            [
                KeyboardButton(text="Profile"),
                KeyboardButton(text="About us")
            ],
        ],
        resize_keyboard=True,
    )

    return keyboard