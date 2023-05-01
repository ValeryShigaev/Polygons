from .geojson_serializers import MultiPolygonsSerializer, MultiPointsSerializer
from sqlalchemy.engine.result import ScalarResult

mp = MultiPolygonsSerializer("MultiPolygon")
mpt = MultiPointsSerializer("Point")


async def poly_to_geojson(db_data: ScalarResult):
    return await mp.serialize(db_data, ["id"])


async def points_to_geojson(db_data: ScalarResult):
    return await mpt.serialize(db_data,
                               ["id", "name", "pop_max", "featurecla"])



