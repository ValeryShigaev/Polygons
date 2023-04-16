from .base import GeojsonBase
from utils import get_coordinates
from sqlalchemy.engine.result import ScalarResult


class MultiPolygonsSerializer(GeojsonBase):

    def serialize(self, obj: ScalarResult):
        # index = 0
        geojson = self.struct.copy()
        for polygon in list(obj):
            print(polygon.id)
            new_feature = {"type": "Feature",
                        "properties": {},
                        "geometry": {"type":
                                     "MultiPolygon",
                                     "coordinates": [[[]]]
                                     }
                        }
            new_feature["properties"]["id"] = polygon.id
            print(get_coordinates(polygon.geom))
            for c in get_coordinates(polygon.geom):
                new_feature["geometry"]["coordinates"][0][0].append(list(c))
            geojson["features"].append(new_feature)
            print(new_feature)
        # for c in get_coordinates(polygon.geom)[0][0]:
        #     geojson["features"][index]["geometry"]["coordinates"][0][
        #         0].append(list(c))
        #     index += 1
        return geojson

