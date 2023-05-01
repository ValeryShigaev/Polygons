import copy
import json

from .base import GeojsonBase
from utils import get_coordinates
from sqlalchemy.engine.result import ScalarResult


class MultiPolygonsSerializer(GeojsonBase):

    async def serialize(self, *args):
        # geojson = copy.deepcopy(self.struct)
        # for polygon in list(obj):
        #     new_feature = copy.deepcopy(self.pol_feature)
        #     new_feature["properties"]["id"] = polygon.id
        #     for c in get_coordinates(polygon.geom, "Polygon"):
        #         new_feature["geometry"]["coordinates"][0][0].append(list(c))
        #     geojson["features"].append(new_feature)
        # return geojson
        return await super().serialize(*args)


class MultiPointsSerializer(GeojsonBase):

    # async def serialize(self, obj: ScalarResult):
    #     geojson = copy.deepcopy(self.struct)
    #     print(obj)
    #     for polygon in list(obj):
    #         print(polygon)
    #         new_feature = copy.deepcopy(self.pt_feature)
    #         new_feature["properties"]["id"] = polygon.id
    #         new_feature["properties"]["name"] = polygon.name
    #         new_feature["properties"]["pop_max"] = polygon.pop_max
    #         new_feature["properties"]["featurecla"] = polygon.featurecla
    #         for c in get_coordinates(polygon.geom, "Point"):
    #             new_feature["geometry"]["coordinates"].append(c)
    #         geojson["features"].append(new_feature)
    #     return geojson
    async def serialize(self, *args):
        return await super().serialize(*args)
