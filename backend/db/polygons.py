from sqlalchemy import select
from sqlalchemy.engine.result import ScalarResult
from sqlalchemy import event

from models.models import Poly
from .base import BaseManager
from .exceptions import all_methods_control, db_control
from utils import get_coordinates, get_WKB
from geoalchemy2.elements import WKBElement


@all_methods_control(db_control)
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
                             latlng: list[float]) -> bool:
        poly = await self.get_polygons(fid=fid)
        updated_geom = await self.update_geometry(poly, v_index, latlng)
        async with self.async_session() as session:
            try:
                current = await session.execute(select(Poly).where(Poly.id
                                                                   == fid))
                current = current.scalars().one()
                current.geom = updated_geom
                await session.commit()
                return True
            except Exception as e:
                print(e)
                await session.rollback()
                return False

    @classmethod
    @db_control
    async def update_geometry(cls, polygon: ScalarResult, v_index: int,
                              latlng: list[float]) -> WKBElement:
        geometry = list(polygon)[0].geom
        coordinates = await get_coordinates(geometry, "MultiPolygon")
        coordinates = list(coordinates)[:-1]
        coordinates[v_index] = tuple(latlng)
        return await get_WKB(tuple(coordinates))







