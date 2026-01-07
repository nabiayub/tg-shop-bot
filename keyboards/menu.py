from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Catalog")],
            [
                KeyboardButton(text="Profile"),
                KeyboardButton(text="About us")
            ],
        ],
        resize_keyboard=True,
    )