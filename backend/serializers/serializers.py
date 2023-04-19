from .geojson_serializers import MultiPolygonsSerializer
from sqlalchemy.engine.result import ScalarResult

mp = MultiPolygonsSerializer("MultiPolygon")


async def poly_to_geojson(db_data: ScalarResult):
    return await mp.serialize(db_data)



