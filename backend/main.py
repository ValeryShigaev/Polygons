from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import poly_manager as pm
from db import point_manager as ptm
from serializers import poly_to_geojson, points_to_geojson
from utils import get_coordinates

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


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


@app.get("/places")
async def get_places():
    db_data = await ptm.get_places()
    return await points_to_geojson(db_data)


@app.get("/poly_info/{poly_id}")
async def poly_info(poly_id: int):
    db_data = await pm.get_polygons(fid=poly_id)
    print(db_data)
    for item in list(db_data):
        coords = list(get_coordinates(item.geom, "MultiPolygon"))[:-1]
        print(coords)
    polygon = Polygon(coords)
    print(polygon)
    points_data = await ptm.get_places()
    points_list = list()
    for item in list(points_data):
        coords = list(get_coordinates(item.geom, "Point"))
        points_list.append(Point(coords))
    indexes = list()
    for index, point in enumerate(points_list, 1):
        if polygon.contains(point):
            indexes.append(index)
    print(indexes)
    print(len(indexes))
    result = await ptm.get_places(indexes)
    for item in list(result):
        print(item.name)




# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
