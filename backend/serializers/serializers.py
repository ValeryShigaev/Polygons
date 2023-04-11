import json

from sqlalchemy.engine.result import ScalarResult

from utils import get_coordinates


def poly_geojson(db_data: ScalarResult):
    geojson = {
        "type": "FeatureCollection",
        "crs": {"type": "name",
                "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
        "features": []
    }
    index = 0
    for polygon in db_data:
        fid = polygon.id
        geojson["features"].append({"type": "Feature",
                                    "properties": {"id": fid},
                                    "geometry": {"type": "MultiPolygon",
                                                 "coordinates": []}}
                                   )
        for c in get_coordinates(polygon.geom)[0][0]:
            geojson["features"][index]["geometry"]["coordinates"].append(list(c))
        index += 1
    return geojson


