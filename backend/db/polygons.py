from sqlalchemy import select
from sqlalchemy.engine.result import ScalarResult

from models.models import Poly
from .base import BaseManager


class PolyManager(BaseManager):

    async def get_polygons(self, fid: int = None) -> ScalarResult:
        async with self.async_session() as session:
            async with session.begin():
                if fid:
                    statement = select(Poly).where(Poly.id == fid)
                else:
                    statement = select(Poly)
                polygons = await session.execute(statement)
        return polygons.scalars()
