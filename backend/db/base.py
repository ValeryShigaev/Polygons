from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from .engine import DATABASE_URL


class BaseManager:
    def __init__(self):
        self.engine = create_async_engine(DATABASE_URL, future=True,
                                          echo=True)
        self.async_session = sessionmaker(self.engine, expire_on_commit=False,
                                          class_=AsyncSession)
