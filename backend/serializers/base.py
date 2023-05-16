import copy

from sqlalchemy.engine.result import ScalarResult

from utils import get_coordinates
from .exceptions import serializer_control


class GeojsonBase:
    """
    This class is used to serialize such geometry as Points and Multipolygons
    which are stored in a Postgres database with the PostGIS extension. During
    initialization, the geometry type is Point or Multipolygon. The serialize
    method receives data of the ScalarResult type as input, as well as a list
    of fields that need to be serialized.
    Args:
        geometry: Point or MultiPolygon
        :type geometry: str
        struct: GeoJson structure
        :type struct: dict
        pol_feature: structure of Multipolygon feature
        :type pol_feature: dict
        pt_feature: structure of Point feature
        :type pt_feature: dict
    Methods:
        serialize: this method used to serialize ScalarResult to GeoJson,
            receives data of the ScalarResult type as input, as well as a list
            of fields that need to be serialized
        serialize_feature: creates separate features for each feature in
            the data
        get_values: this class method returns a dict of model fields and values
        check_geometry: checks if geometry supported
    """

    def __init__(self, geometry: str):
        self.geometry = geometry
        self.struct = {"type": "FeatureCollection",
                       "crs": {"type": "name",
                               "properties": {"name":
                                              "urn:ogc:def:crs:OGC:"
                                              "1.3:CRS84"}
                               },
                       "features": []
                       }
        self.pol_feature = {"type": "Feature",
                            "properties": {},
                            "geometry": {"type":
                                         f"{geometry}",
                                         "coordinates": [[[]]]
                                         }
                            }
        self.pt_feature = {"type": "Feature",
                           "properties": {},
                           "geometry": {"type":
                                        f"{geometry}",
                                        "coordinates": []
                                        }
                           }
        self.check_geometry()

    @serializer_control
    async def serialize(self, obj: ScalarResult, fields: list[str]) -> dict:
        geojson = copy.deepcopy(self.struct)
        for feature in list(obj):
            if self.geometry == "Point":
                new_feature = await self.serialize_feature(feature,
                                                           fields,
                                                           copy.deepcopy(
                                                               self.pt_feature)
                                                           )
                geojson["features"].append(new_feature)
            elif self.geometry == "MultiPolygon":
                new_feature = await self.serialize_feature(feature,
                                                           fields,
                                                           copy.deepcopy(
                                                               self.pol_feature)
                                                           )
                geojson["features"].append(new_feature)
        return geojson

    async def serialize_feature(self, feature, fields, new_feature):
        for field in fields:
            f_fields = await self.get_values(feature)
            new_feature["properties"][field] = f_fields[field]
        coordinates = await get_coordinates(feature.geom, self.geometry)
        for c in coordinates:
            if self.geometry == "Point":
                new_feature["geometry"]["coordinates"].append(c)
            elif self.geometry == "MultiPolygon":
                new_feature["geometry"]["coordinates"][0][0].append(c)
        return new_feature

    @classmethod
    async def get_values(cls, model) -> dict:
        return dict((column.name, getattr(model, column.name))
                    for column in model.__table__.columns)

    def check_geometry(self):
        if self.geometry not in ["MultiPolygon", "Point"]:
            raise Exception("Only 'Point' or 'MultiPolygon' types "
                            "are supported")
