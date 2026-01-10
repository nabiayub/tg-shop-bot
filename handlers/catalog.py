from aiogram import F, Router, types
from sqlalchemy import ScalarResult

from database import Book, Category
from keyboards.catalog import generate_catalog_kb, CategoryCBData, generate_books_kb, BookCBData, \
    back_to_category_books_kb
from repositories.books import BookRepo
from repositories.categories import CategoryRepo

router = Router()


@router.callback_query(F.data == 'catalog')
@router.message(F.text == 'Catalog')
async def catalog(
        update: types.Message | types.CallbackQuery,
        category_repo: CategoryRepo):
    """
    Handler for Catalog menu:
    - Sends all categories
    - Edit message for callback query updates (the Back button)
    """

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
async def category_info(
        callback: types.CallbackQuery,
        callback_data: CategoryCBData,
        category_repo: CategoryRepo,
        book_repo: BookRepo):
    """
    Handler for viewing a specific catalog category.

    Steps:
    1. Extract the category key from the callback data.
    2. Retrieve the category information from CATALOG.
    3. Edit the original message with the category description.
    4. Provide a 'Back' button to return to the main catalog.
    """

    category: Category = await category_repo.get_category_by_id(callback_data.category_id)
    books: ScalarResult[Book] = await book_repo.get_books_by_categorie_id(callback_data.category_id)

    await callback.message.edit_text(
        text=category.description,
        reply_markup=generate_books_kb(books=books)
    )


@router.callback_query(BookCBData.filter())
async def book_info(
        callback: types.CallbackQuery,
        callback_data: BookCBData,
        book_repo: BookRepo, ):
    """
    Handler for viewing a specific book information.
    :param callback: types.CallbackQuery
    :param callback_data: object of BookCBData
    :param book_repo: object of BookRepo
    """
    book_id = callback_data.book_id
    book: Book = await book_repo.get_book_by_id(book_id)

    await callback.message.edit_text(
        f'Name - {book.name.format(book_id)}\n'
        f'Description - {book.description}\n'
        f'Price - {book.price} dollars\n\n'
        'Do you want to buy this book?',
        reply_markup=back_to_category_books_kb(
            category_id=book.category_id,
            book_id=book.id,)
    )
