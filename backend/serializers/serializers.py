""" Here is project serializers """

import json

from sqlalchemy.engine.result import ScalarResult

from .geojson_serializers import Serializer

mp = Serializer("MultiPolygon")
mpt = Serializer("Point")


async def poly_to_geojson(db_data: ScalarResult) -> json:
    """
    Returns polygons in GeoJson format

    :param db_data: polygons from db
    :type db_data: ScalarResult
    :rtype: json
    """

    return await mp.serialize(db_data, ["id"])


async def points_to_geojson(db_data: ScalarResult) -> json:
    """
    Returns points in GeoJson format

    :param db_data: points from db
    :type db_data: ScalarResult
    :rtype: json
    """

    return await mpt.serialize(db_data,
                               ["id", "name", "pop_max", "featurecla"])


async def inside_the_polygon(polygon: ScalarResult,
                             points: ScalarResult) -> dict:
    """
    Returns the data about points that are in the polygon

    :param polygon: input polygon
    :type polygon: ScalarResult
    :param points: all points (places) from db
    :type points: ScalarResult
    :rtype: dict
    """

    return await mpt.serialize_inters_results(polygon, points)
