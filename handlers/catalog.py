from aiogram import F, Router, types

from database import Category
from keyboards.catalog import generate_catalog_kb, CategoryCBData, generate_books_kb, BookCBData, back_to_category_books
from repositories.categories import CategoryRepo

router = Router()


CATALOG = {
    'romans': {
        'text': 'Romans',
        'description': 'Romans books',
        'books': [
            {'id': 1, 'name': 'Book {}', 'description': 'Book description {}', 'price': 100},
            {'id': 2, 'name': 'Book {}', 'description': 'Book description {}', 'price': 200},
            {'id': 3, 'name': 'Book {}', 'description': 'Book description {}', 'price': 300},
        ]
    },

    'fantasies': {
        'text': 'Fantasy',
        'description': 'Fantasy books',
        'books': [
            {'id': 1, 'name': 'Book {}', 'description': 'Book description {}', 'price': 100},
            {'id': 2, 'name': 'Book {}', 'description': 'Book description {}', 'price': 200},
            {'id': 3, 'name': 'Book {}', 'description': 'Book description {}', 'price': 300},
        ]
    },

    'horrors': {
        'text': 'Horror',
        'description': 'Horror books',
        'books': [
            {'id': 1, 'name': 'Book {}', 'description': 'Book description {}', 'price': 100},
            {'id': 2, 'name': 'Book {}', 'description': 'Book description {}', 'price': 200},
            {'id': 3, 'name': 'Book {}', 'description': 'Book description {}', 'price': 300},
        ]
    },

    'detectives': {
        'text': 'Detective',
        'description': 'Detective books',
        'books': [
            {'id': 1, 'name': 'Book {}', 'description': 'Book description {}', 'price': 100},
            {'id': 2, 'name': 'Book {}', 'description': 'Book description {}', 'price': 200},
            {'id': 3, 'name': 'Book {}', 'description': 'Book description {}', 'price': 300},
        ]
    },

    'documentaries': {
        'text': 'Documentary',
        'description': 'Documentary books',
        'books': [
            {'id': 1, 'name': 'Book {}', 'description': 'Book description {}', 'price': 100},
            {'id': 2, 'name': 'Book {}', 'description': 'Book description {}', 'price': 200},
            {'id': 3, 'name': 'Book {}', 'description': 'Book description {}', 'price': 300},
        ]
    },
}


@router.callback_query(F.data == 'catalog')
@router.message(F.text == 'Catalog')
async def catalog(update: types.Message | types.CallbackQuery, category_repo: CategoryRepo):
    '''
    Handler for Catalog menu:
    - Sends all categories
    - Edit message for callback query updates (the Back button)
    '''

    categories = await category_repo.get_all_categories()

    if isinstance(update, types.Message):
        await update.answer(
            'Our catalog:',
            reply_markup=generate_catalog_kb(categories)
        )
    else:
        await update.message.edit_text(
            'Our catalog:',
            reply_markup=generate_catalog_kb(categories)
        )


@router.callback_query(CategoryCBData.filter())
async def category_info(callback: types.CallbackQuery, callback_data: CategoryCBData, category_repo: CategoryRepo):
    '''
    Handler for viewing a specific catalog category.

    Steps:
    1. Extract the category key from the callback data.
    2. Retrieve the category information from CATALOG.
    3. Edit the original message with the category description.
    4. Provide a 'Back' button to return to the main catalog.
    '''

    category: Category = category_repo.get_category_by_id(callback_data.category_id)

    await callback.message.edit_text(
        text=category.description,
        reply_markup=generate_books_kb(
            books=category['books'],
            category=callback_data.category
        )
    )

@router.callback_query(BookCBData.filter())
async def book_info(callback: types.CallbackQuery, callback_data: BookCBData):
    '''
    Handler for viewing a specific book information.
    :param callback: types.CallbackQuery
    :param callback_data: object of BookCBData
    '''
    book_id = callback_data.id
    category = CATALOG.get(callback_data.category)

    book = None

    for bk in category['books']:
        if bk['id'] == book_id:
            book = bk
            break

    if not book:
        return await callback.answer('Book not found')

    await callback.message.edit_text(
        f'Name - {book["name"].format(book_id)}\n'
        f'Description - {book["description"].format(book_id)}\n'
        f'Price - {book["price"]} dollars\n\n'
        'Do you want to buy this book?',
        reply_markup=back_to_category_books(callback_data.category)
    )

