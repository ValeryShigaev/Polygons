from .geojson_serializers import MultiPolygonsSerializer
from sqlalchemy.engine.result import ScalarResult

mp = MultiPolygonsSerializer()


def poly_to_geojson(db_data: ScalarResult):
    return mp.serialize(db_data)



