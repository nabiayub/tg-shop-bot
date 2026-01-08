from aiogram import Dispatcher

from middlewares.session import DatabaseSessionMiddleware


def register_middlewares(dp: Dispatcher, session_maker) -> None:
    '''
    Registers all middlewares for the dispatcher.

    :param dp: Aiogram Dispatcher instance
    :param session_maker: SQLAlchemy session factory for database access
    '''
    dp.update.middleware(DatabaseSessionMiddleware(session_maker))
