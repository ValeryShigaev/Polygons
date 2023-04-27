from sqlalchemy import select
from sqlalchemy.engine.result import ScalarResult

from models.models import Places
from .base import BaseManager


class PointManager(BaseManager):

    async def get_places(self) -> ScalarResult:
        async with self.async_session() as session:
            async with session.begin():
                statement = (select(Places))
                points = await session.execute(statement)
        return points.scalars()
