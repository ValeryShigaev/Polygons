from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

from db import point_manager as ptm
from utils import get_coordinates, get_intersection_indexes

from .base import GeojsonBase


class Serializer(GeojsonBase):

    async def serialize(self, *args):
        return await super().serialize(*args)

    async def serialize_inters_results(self, polygon, points):
        indexes = await self.get_indexes(polygon, points)
        places = await ptm.get_places(indexes)
        result = {"places": list(), "pop": 0}
        for item in list(places):
            result["places"].append(item.name)
            result["pop"] += item.pop_max
        return result

    @classmethod
    async def get_indexes(cls, polygon, points):
        indexes = await get_intersection_indexes(list(polygon),
                                                 list(points),)
        return indexes

