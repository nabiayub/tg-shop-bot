from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


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
                    callback_data=f'category:{category_cb}'
                )
            ]
        )

    return keyboard