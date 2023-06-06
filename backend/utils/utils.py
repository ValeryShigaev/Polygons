from binascii import unhexlify
from typing import List

from geoalchemy2.elements import WKBElement
from shapely import wkb, wkt
from shapely.geometry import MultiPolygon, Point, mapping
from shapely.geometry.polygon import Polygon


async def get_coordinates(geom: WKBElement, geom_name: str) -> List:
    bytes_geom = unhexlify(str(geom))
    wkb_geom = wkb.loads(bytes_geom)
    if geom_name == "MultiPolygon":
        return mapping(wkb_geom)["coordinates"][0][0]
    elif geom_name == "Point":
        return mapping(wkb_geom)["coordinates"]


async def get_WKB(coordinates: tuple):
    print(coordinates)
    polygon = MultiPolygon([Polygon(coordinates)])
    new = wkb.dumps(polygon, hex=True, srid=4326)
    return new


async def get_intersection_indexes(polygon: list,
                                   points: list[Point]) -> list[int]:
    indexes = list()
    coords = list()
    points_list = list()
    for item in polygon:
        result_coords = await get_coordinates(item.geom, "MultiPolygon")
        coords = list(result_coords)[:-1]
    p = Polygon(coords)
    for item in points:
        result_coords = await get_coordinates(item.geom, "Point")
        points_list.append(Point(result_coords))
    for index, point in enumerate(points_list, 1):
        if p.contains(point):
            indexes.append(index)
    return indexes


