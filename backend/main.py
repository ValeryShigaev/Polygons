from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import poly_manager as pm
from serializers import poly_to_geojson


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def get_poly():
    db_data = await pm.get_polygons()
    return await poly_to_geojson(db_data)



# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
