from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from database.models.user import User
from database.models.category import Category
from database.models.book import Book

from config.settings import DATABASE_URL


engine = create_async_engine(
    # url=DATABASE_URL,
    url='sqlite+aiosqlite:///book_shop.db',
)

session_maker = async_sessionmaker(engine, expire_on_commit=False)

__all__ = [
    'User',
    'Category',
    'Book',
]