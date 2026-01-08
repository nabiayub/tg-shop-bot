from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


class CategoryCBData(CallbackData, prefix='category'):
    '''Callback data for selecting a book category'''
    category: str


def generate_catalog_kb(catalog: dict) -> InlineKeyboardMarkup:
    '''
    Generate a inline keyboard for the Telegram bot catalog
    :param catalog:
        catalog: A dictionary where keys are callbak IDs and valuesa are
                dictionary with cateogry information.
    :return:
        InlineKeyboardMarkup: Inline keyboard with buttons
    '''
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])

    for category_cb, category in catalog.items():
        keyboard.inline_keyboard.append(
            [
                InlineKeyboardButton(
                    text=category['text'],
                    callback_data=CategoryCBData(category=category_cb).pack()
                )
            ]
        )

    return keyboard