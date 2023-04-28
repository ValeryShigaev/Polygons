from typing import List
from shapely import wkb, wkt
from shapely.geometry import mapping
from binascii import unhexlify
from geoalchemy2.functions import (ST_AsText, ST_GeometryType,
                                   ST_GeomFromWKB, ST_AsGeoJSON)
from geoalchemy2.elements import WKBElement
from geoalchemy2.shape import to_shape


def get_coordinates(geom: WKBElement, geom_name: str) -> List:
    bytes_geom = unhexlify(str(geom))
    wkb_geom = wkb.loads(bytes_geom)
    if geom_name == "MultiPolygon":
        return mapping(wkb_geom)["coordinates"][0][0]
    elif geom_name == "MultiPoint":
        return mapping(wkb_geom)["coordinates"]
