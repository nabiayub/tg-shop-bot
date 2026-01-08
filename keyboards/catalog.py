from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
from typing import List, Dict


class CategoryCBData(CallbackData, prefix='category'):
    '''Callback data for selecting a book category'''
    category: str


class BookCBData(CallbackData, prefix='book'):
    '''Callback data for selecting a book'''
    id: int
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


def generate_books_kb(books: List[Dict[str, int | str]], category: str) -> InlineKeyboardMarkup:
    '''
    Generate a inline keyboard for the Telegram bot catalog for book list
    :param books: List of dictionaries, each containing book information.
                  Each dictionary should have at least the keys:
                  - 'id' (int): Unique book ID
                  - 'name' (str): Book name
                  - 'description' (str): Book description
                  - 'price' (int): Book price
    :param category: string name of the category
    :return: Inline keyboard with buttons as book names
    '''
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])

    for book in books:
        keyboard.inline_keyboard.append(
            [
                InlineKeyboardButton(
                    text=book['name'].format(book['id']),
                    callback_data=BookCBData(id=book['id'], category=category).pack()

                )
            ]
        )

    keyboard.inline_keyboard.append(
        [
            InlineKeyboardButton(text='<< Back', callback_data='catalog')
        ]
    )

    return keyboard


def back_to_category_books(category: str) -> InlineKeyboardMarkup:
    '''
    Generate a back button for Book view to return to Books of Category
    :param category: string name of the category
    :return: Inline keyboard with one button
    '''
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Back',
                    callback_data=CategoryCBData(category=category).pack()
                )
            ]
        ]
    )
