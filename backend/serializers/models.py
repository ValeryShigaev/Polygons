from typing import Dict, Optional

from geoalchemy2.elements import WKBElement
from geojson_pydantic import FeatureCollection, Polygon
from pydantic import BaseModel, PositiveInt, validator


class DataToUpdate(BaseModel):
    poly_id: int
    vertex_id: int
    latlng: list[float]
