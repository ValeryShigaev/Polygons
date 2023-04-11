from typing import Optional, Dict

from pydantic import BaseModel, PositiveInt, validator

from geojson_pydantic import FeatureCollection, Polygon

from geoalchemy2.elements import WKBElement


class PolygonsResult(BaseModel):
    id: int