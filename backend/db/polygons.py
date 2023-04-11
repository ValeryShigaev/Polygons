from sqlalchemy import select

from models.models import Poly
from .base import BaseManager


class PolyManager(BaseManager):

    async def get_polygons(self):
        async with self.async_session() as session:
            async with session.begin():
                statement = (select(Poly))
                polygons = await session.execute(statement)
        print(type(polygons.scalars()))
        return polygons.scalars()
