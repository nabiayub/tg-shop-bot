from aiogram import F, Router, types

from keyboards.catalog import generate_catalog_kb, CategoryCBData, generate_books_kb

router = Router()

# CATALOG = {
#     'romans':
#         {
#             'text': 'Romans',
#             'description': 'Romans books',
#             'books': [
#                 {
#                     'id': 1,
#                     'name': 'Book {}',
#                     'description': 'Book description {}',
#                     'price': 100
#                 },
#
#                 {
#                     'id': 2,
#                     'name': 'Book {}',
#                     'description': 'Book description {}',
#                     'price': 200
#                 },
#                 {
#                     'id': 3,
#                     'name': 'Book {}',
#                     'description': 'Book description {}',
#                     'price': 300
#                 },
#             ]
#         },
#     'fantasies': {'text': 'Fantasy', 'description': 'Fantasy books'},
#     'horrors': {'text': 'Horror', 'description': 'Horror books'},
#     'detectives': {'text': 'Detective', 'description': 'Detective books'},
#     'documentaries': {'text': 'Documentary', 'description': 'Documentary books'},
# }

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
async def catalog(update: types.Message | types.CallbackQuery):
    '''
    Handler for Catalog menu:
    - Sends all categories
    - Edit message for callback query updates (the Back button)
    '''
    if isinstance(update, types.Message):
        await update.answer(
            'Our catalog:',
            reply_markup=generate_catalog_kb(CATALOG)
        )
    else:
        await update.message.edit_text(
            'Our catalog:',
            reply_markup=generate_catalog_kb(CATALOG)
        )


@router.callback_query(CategoryCBData.filter())
async def catalog_info(callback: types.CallbackQuery, callback_data: CategoryCBData):
    '''
    Handler for viewing a specific catalog category.

    Steps:
    1. Extract the category key from the callback data.
    2. Retrieve the category information from CATALOG.
    3. Edit the original message with the category description.
    4. Provide a 'Back' button to return to the main catalog.
    '''

    category = CATALOG.get(callback_data.category)

    await callback.message.edit_text(
        text=category['description'],
        reply_markup=generate_books_kb(
            books=category['books'],
            category=callback_data.category
        )
    )
