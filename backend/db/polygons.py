from sqlalchemy import select
from sqlalchemy.engine.result import ScalarResult

from models.models import Poly
from .base import BaseManager
from utils import get_coordinates, get_WKB


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

    async def update_polygon(self, fid: int, v_index: int,
                             latlng: list[float]):
        poly = await self.get_polygons(fid=fid)
        geometry = list(poly)[0].geom
        coordinates = await get_coordinates(geometry, "MultiPolygon")
        coordinates = list(coordinates)[:-1]
        coordinates[v_index] = tuple(latlng)
        coordinates = tuple(coordinates)
        print(coordinates)
        updated_geom = await get_WKB(coordinates)
        print(updated_geom)
        async with self.async_session() as session:
            current = await session.execute(select(Poly).where(Poly.id == fid))
            current = current.scalars().one()
            current.geom = updated_geom
            await session.commit()


