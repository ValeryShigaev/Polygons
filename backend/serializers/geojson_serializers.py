from .base import GeojsonBase
from utils import get_coordinates
from db import point_manager as ptm

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


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
        coords = list()
        for item in list(polygon):
            coords = list(get_coordinates(item.geom, "MultiPolygon"))[:-1]
        temp_polygon = Polygon(coords)
        points_list = list()
        for item in list(points):
            coords = list(get_coordinates(item.geom, "Point"))
            points_list.append(Point(coords))
        indexes = list()
        for index, point in enumerate(points_list, 1):
            if temp_polygon.contains(point):
                indexes.append(index)
        return indexes

