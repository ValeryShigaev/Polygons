from abc import ABC


class GeojsonBase(ABC):

    def __init__(self, geometry: str):
        self.struct = {"type": "FeatureCollection",
                       "crs": {"type": "name",
                               "properties": {"name":
                                              "urn:ogc:def:crs:OGC:"
                                              "1.3:CRS84"}
                               },
                       "features": []
                       }
        self.feature = {"type": "Feature",
                        "properties": {},
                        "geometry": {"type":
                                     f"{geometry}",
                                     "coordinates": [[[]]]
                                     }
                        }

    async def serialize(self, obj):
        pass
