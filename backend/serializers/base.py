from abc import ABC
import copy

from sqlalchemy.engine.result import ScalarResult

from utils import get_coordinates


class GeojsonBase(ABC):

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

    async def serialize(self, obj: ScalarResult, fields: list[str]):
        geojson = copy.deepcopy(self.struct)
        for feature in list(obj):
            if self.geometry == "MultiPoint":
                new_feature = copy.deepcopy(self.pol_feature)
                for field in fields:
                    f_fields = await self.get_values(feature)
                    new_feature["properties"][field] = f_fields[field]
                for c in get_coordinates(feature.geom, self.geometry):
                    new_feature["geometry"]["coordinates"].append(c)
                geojson["features"].append(new_feature)
        return geojson

    @classmethod
    async def get_values(cls, model):
        return dict((column.name, getattr(model, column.name))
                    for column in model.__table__.columns)




