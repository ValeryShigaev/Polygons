""" Database manager class that is responsible for working with polygons """

from geoalchemy2.elements import WKBElement
from sqlalchemy import event, select
from sqlalchemy.engine.result import ScalarResult

from models.models import Poly
from utils import get_coordinates, get_WKB

from .base import BaseManager
from .exceptions import all_methods_control, db_control


@all_methods_control(db_control)
class PolyManager(BaseManager):
    """
    Class that is responsible for working with polygons
    Parent: BaseManager
    Methods:
        get_polygons: this method allows to get polygons from database
        update_polygon: this method allows to update polygon vertex
        update_geometry: this method allows to update polygon geometry
    """

    async def get_polygons(self, fid: int = None) -> ScalarResult:
        """
        This method allows to get polygons or one of them if "fid" is selected

        :param fid: polygon id
        :type fid: int
        :rtype: ScalarResult
        """

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
        """
        This transaction allows to update geometry of polygon

        :param fid: polygon id
        :type fid: int
        :param v_index: id of updated vertex
        :type v_index: int
        :param latlng: list of new vertex coordinates
        :type latlng: list[float]
        :rtype: bool
        """

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
        """
        This method returns the new polygon geometry in WKB format

        :param polygon: polygon for update
        :type polygon: ScalarResult
        :param v_index: id of updated vertex
        :type v_index: int
        :param latlng: list of new vertex coordinates
        :type latlng: list[float]
        :rtype: WKBElement
        """

        geometry = list(polygon)[0].geom
        coordinates = await get_coordinates(geometry, "MultiPolygon")
        coordinates = list(coordinates)[:-1]
        coordinates[v_index] = tuple(latlng)
        return await get_WKB(tuple(coordinates))
