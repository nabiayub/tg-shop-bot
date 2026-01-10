from typing import List

from sqlalchemy import select, ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.book import Book

class BookRepo:
    def __init__(self, session: AsyncSession):
        self.__session = session

    async def get_books_by_categorie_id(self, category_id: int) -> ScalarResult[Book]:
        statement = select(Book).where(Book.category_id == category_id)
        return await self.__session.scalars(statement)

    async def get_book_by_id(self, book_id: int) -> Book:
        """
        Fetches a book from Book table using ID
        :param book_id: int ID of book
        :return: object of Book model
        """
        statement = select(Book).where(Book.id == book_id)
        return await self.__session.scalar(statement)

