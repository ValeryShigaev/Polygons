""" Here is the main project serializer class """

from sqlalchemy.engine.result import ScalarResult

from db import point_manager as ptm
from utils import get_coordinates, get_intersection_indexes

from .base import GeojsonBase


class Serializer(GeojsonBase):
    """
    This class is used for serialize data (points within a polygon)
    Parent: GeojsonBase

    Methods:
        serialize_inters_results: this method allows to find points in a
                                  polygon and return data on them
        get_indexes: this method allows to get indexes of the points inside
                     polygon
    """

    async def serialize(self, *args):
        return await super().serialize(*args)

    async def serialize_inters_results(self, polygon: ScalarResult,
                                       points: ScalarResult) -> dict:
        """
        This method allows to find points in a polygon and return data on them

        :param polygon: input polygon
        :type polygon: ScalarResult
        :param points: all points (places)
        :type points: ScalarResult
        :rtype: dict
        """

        indexes = await self.get_indexes(polygon, points)
        places = await ptm.get_places(indexes)
        result = {"places": list(), "pop": 0}
        for item in list(places):
            result["places"].append(item.name)
            result["pop"] += item.pop_max
        return result

    @classmethod
    async def get_indexes(cls, polygon: ScalarResult,
                          points: ScalarResult) -> list[int]:
        """
        This method allows to get indexes of the points inside polygon

        :param polygon: input polygon
        :type polygon: ScalarResult
        :param points: all points (places)
        :type points: ScalarResult
        :rtype: list[int]
        """

        indexes = await get_intersection_indexes(list(polygon),
                                                 list(points),)
        return indexes

