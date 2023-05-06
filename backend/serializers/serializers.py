from .geojson_serializers import Serializer
from sqlalchemy.engine.result import ScalarResult

mp = Serializer("MultiPolygon")
mpt = Serializer("Point")


async def poly_to_geojson(db_data: ScalarResult):
    return await mp.serialize(db_data, ["id"])


async def points_to_geojson(db_data: ScalarResult):
    return await mpt.serialize(db_data,
                               ["id", "name", "pop_max", "featurecla"])



