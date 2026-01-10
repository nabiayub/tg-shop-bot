from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
from typing import List, Dict

from sqlalchemy import ScalarResult

from database import Category
from database.models import book
from repositories.categories import CategoryRepo


class CategoryCBData(CallbackData, prefix='category'):
    '''Callback data for selecting a book category'''
    category_id: int


class BookCBData(CallbackData, prefix='book'):
    '''Callback data for selecting a book'''
    book_id: int

class BuyBookCBData(CallbackData, prefix='buy_book'):
    book_id: int


def generate_catalog_kb(categories: ScalarResult[Category]) -> InlineKeyboardMarkup:

    '''
    Generate a inline keyboard for the Telegram bot catalog
    :param categories: List of categories to generate inline keyboards
    :return: InlineKeyboardMarkup: Inline keyboard with buttons
    '''
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])

    for category in categories:
        keyboard.inline_keyboard.append(
            [
                InlineKeyboardButton(
                    text=category.name,
                    callback_data=CategoryCBData(category_id=category.id).pack()
                )
            ]
        )

    return keyboard


def generate_books_kb(books) -> InlineKeyboardMarkup:
    '''
    Generate a inline keyboard for the Telegram bot catalog for book list
    :param books:
    :return: Inline keyboard with buttons as book names
    '''
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])

    for book in books:
        keyboard.inline_keyboard.append(
            [
                InlineKeyboardButton(
                    text=book.name.format(book.id),
                    callback_data=BookCBData(book_id=book.id).pack()

                )
            ]
        )

    keyboard.inline_keyboard.append(
        [
            InlineKeyboardButton(text='<< Back', callback_data='catalog')
        ]
    )

    return keyboard


def back_to_category_books_kb(
        category_id: int,
        book_id: int) -> InlineKeyboardMarkup:
    '''
    Generate a back button for Book view to return to Books of Category
    :param category_id: int id of the category
    :param book_id: int id of the book
    :return: Inline keyboard with buttons back and buy
    '''
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Buy',
                    callback_data=BuyBookCBData(book_id=book_id).pack()
                )
            ],
            [
                InlineKeyboardButton(
                    text='Back',
                    callback_data=CategoryCBData(category_id=category_id).pack()
                )
            ]
        ]
    )


