""" Pydantic models """

from pydantic import BaseModel, PositiveInt, validator


class DataToUpdate(BaseModel):
    poly_id: int
    vertex_id: int
    latlng: list[float]
