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


def cancel_deposit_action_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text='Cancel',
            callback_data='cancel_deposit'
        )]
    ])


def apply_deposit_action_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Apply',
                callback_data='apply_deposit'
            ),
            InlineKeyboardButton(
                text='Cancel',
                callback_data='cancel_deposit'
            )
        ],

    ])
