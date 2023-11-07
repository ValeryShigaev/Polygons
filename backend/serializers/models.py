""" Pydantic models """

from typing import List, Any, Optional
from pydantic import BaseModel


class DataToUpdate(BaseModel):
    poly_id: int
    vertex_id: int
    latlng: List[float]


class IntersectionData(BaseModel):
    places: List[str]
    pop: int


class CrsProperties(BaseModel):
    name: str


class Crs(BaseModel):
    type: str
    properties: CrsProperties


class Geometry(BaseModel):
    type: str
    coordinates: List[Any]


class PointFeatureProperties(BaseModel):
    id: int
    name: Optional[str]
    pop_max: Optional[int]
    featurecla: Optional[str]


class PolyFeatureProperties(BaseModel):
    id: int


class Feature(BaseModel):
    type: str
    properties: Any
    geometry: Geometry


class PointFeature(Feature):
    properties: PointFeatureProperties


class PolyFeature(Feature):
    properties: PolyFeatureProperties


class GeoJsonBase(BaseModel):
    type: str
    crs: Crs
    features: List


class GeoJsonPoints(GeoJsonBase):
    features: List[PointFeature]

    class Config:
        orm_mode = True


class GeoJsonPolygons(GeoJsonBase):
    features: List[PolyFeature]

    class Config:
        orm_mode = True
