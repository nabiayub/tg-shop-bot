from typing import Optional

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from database import User


class UserRepo:
    def __init__(self, session: AsyncSession):
        self.__session = session

    async def get_user_by_tg_id(self, tg_id: int) -> Optional[User]:
        """
        Fetch user by telegram ID
        :param self: object
        :param tg_id: integer Telegram ID
        :return: User object
        """
        statement = select(User).where(User.tg_id == tg_id)

        return await self.__session.scalar(statement)

    async def create_or_update_user(self, tg_id: int, username: str, fullname: str) -> None:
        '''
        Create or update user by telegram ID. If user already exists, update it.
        :param tg_id: Telegram ID
        :param fullname: Full name
        :param username: Username
        :return:
        '''
        user = await self.get_user_by_tg_id(tg_id)

        if not user:
            await self.create_user(tg_id=tg_id, username=username, fullname=fullname)
        else:
            user.fullname = fullname
            user.username = username

        await self.__session.commit()

    async def create_user(self, tg_id: int, username: str, fullname: str) -> None:
        """
        Create new user in Users table
        :param tg_id: Telegram ID
        :param username: Telegram username
        :param fullname: Telegram fullname
        """
        user = User(tg_id=tg_id, username=username, fullname=fullname)
        self.__session.add(user)

    async def update_balance(self, tg_id: int, deposit_amount: int) -> None:
        deposit_amount *= 100


        statement = update(User).where(User.tg_id == tg_id).values(
            balance=deposit_amount + User.balance
        )

        await self.__session.execute(statement)
        await self.__session.commit()
