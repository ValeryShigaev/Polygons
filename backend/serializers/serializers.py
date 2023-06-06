from sqlalchemy.engine.result import ScalarResult

from .geojson_serializers import Serializer

mp = Serializer("MultiPolygon")
mpt = Serializer("Point")


async def poly_to_geojson(db_data: ScalarResult):
    return await mp.serialize(db_data, ["id"])


async def points_to_geojson(db_data: ScalarResult):
    return await mpt.serialize(db_data,
                               ["id", "name", "pop_max", "featurecla"])


async def inside_the_polygon(polygon: ScalarResult,
                             points: ScalarResult):
    return await mpt.serialize_inters_results(polygon, points)



