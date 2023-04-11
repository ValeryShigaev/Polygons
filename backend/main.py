from typing import Union

from fastapi import FastAPI

from sqlalchemy import select
from sqlalchemy.orm import Session
from utils.utils import get_coordinates
from db import poly_manager as pm
from serializers import poly_geojson
from geojson_pydantic import FeatureCollection, Polygon


app = FastAPI()


@app.get("/")
async def get_poly():
    db_data = await pm.get_polygons()
    print(db_data)
    print(poly_geojson(db_data))
    return poly_geojson(db_data)


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
