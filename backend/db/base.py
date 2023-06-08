""" Here is a database manager base class """

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from .engine import DATABASE_URL


class BaseManager:
    """
    Database manager base class

    Args:
        :arg self.engine: database manager engine
        :type self.engine: AsyncEngine
        :arg self.async_session: database session
        :type self.async_session: AsyncSession
    """

    def __init__(self):
        self.engine = create_async_engine(DATABASE_URL, future=True,
                                          echo=True)
        self.async_session = sessionmaker(self.engine, expire_on_commit=False,
                                          class_=AsyncSession)
