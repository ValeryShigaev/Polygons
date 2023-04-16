from abc import ABC


class GeojsonBase(ABC):

    def __init__(self):
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
                                     "MultiPolygon",
                                     "coordinates": [[[]]]
                                     }
                        }

    def serialize(self, obj):
        pass
