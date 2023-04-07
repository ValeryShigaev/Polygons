from typing import Optional

from pydantic import BaseModel, PositiveInt, validator

from geojson_pydantic import FeatureCollection, Polygon


class PolygonResult(BaseModel):
    id: PositiveInt

