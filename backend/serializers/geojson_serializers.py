import copy
import json

from .base import GeojsonBase
from utils import get_coordinates
from sqlalchemy.engine.result import ScalarResult


class MultiPolygonsSerializer(GeojsonBase):

    async def serialize(self, obj: ScalarResult):
        geojson = copy.deepcopy(self.struct)
        for polygon in list(obj):
            new_feature = copy.deepcopy(self.feature)
            new_feature["properties"]["id"] = polygon.id
            for c in get_coordinates(polygon.geom):
                new_feature["geometry"]["coordinates"][0][0].append(list(c))
            geojson["features"].append(new_feature)
        return geojson


class MultiPointsSerializer(GeojsonBase):

    async def serialize(self, obj: ScalarResult):
        geojson = copy.deepcopy(self.struct)
        for polygon in list(obj):
            new_feature = copy.deepcopy(self.feature)
            new_feature["properties"]["id"] = polygon.id
            for c in get_coordinates(polygon.geom):
                new_feature["geometry"]["coordinates"][0][0].append(list(c))
            geojson["features"].append(new_feature)
        return geojson

