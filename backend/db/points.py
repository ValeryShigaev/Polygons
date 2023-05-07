from sqlalchemy import select
from sqlalchemy.engine.result import ScalarResult

from models.models import Places
from .base import BaseManager


class PointManager(BaseManager):

    async def get_places(self, indexes: list = None) -> ScalarResult:
        async with self.async_session() as session:
            async with session.begin():
                if indexes:
                    indexes = tuple(indexes)
                    statement = (select(Places).where(Places.id.in_(indexes)))
                else:
                    statement = (select(Places).order_by(Places.id))
                points = await session.execute(statement)
        return points.scalars()

