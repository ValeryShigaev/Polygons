import json

from fastapi import FastAPI

from db import poly_manager as pm
from serializers import poly_to_geojson



app = FastAPI()


@app.get("/")
async def get_poly():
    db_data = await pm.get_polygons()
    response = poly_to_geojson(db_data)
    return response


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
