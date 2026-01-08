from sqlalchemy import select, ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession

from database.models.category import Category

class CategoryRepo:
    def __init__(self, session: AsyncSession):
        self.__session = session

    async def get_all_categories(self) -> ScalarResult[Category]:
        """
        Fetch all categories
        :return:
        """
        statement = select(Category).order_by(Category.name)

        return await self.__session.scalars(statement)

    async def get_category_by_id(self, category_id: int) -> Category:
        """
        Fetch categpry by given id.
        :param category_id: int categoru's ID
        :return:
        """
        statement = select(Category).where(Category.id == category_id)

        return await self.__session.scalar(statement)

    


    