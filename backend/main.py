from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.websockets import WebSocket

from db import point_manager as ptm
from db import poly_manager as pm
from db import sig
from serializers import (DataToUpdate, inside_the_polygon, points_to_geojson,
                         poly_to_geojson)

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
    poly_data = await pm.get_polygons(fid=poly_id)
    points_data = await ptm.get_places()
    return await inside_the_polygon(poly_data, points_data)


@app.post("/poly_update/")
async def poly_update(data: DataToUpdate = Depends()) -> bool:
    result = await pm.update_polygon(data.poly_id, data.vertex_id, data.latlng)
    return result


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json(await get_poly())
    while True:
        await sig.wait()
        if sig:
            await websocket.send_json(await get_poly())
            sig.clear()

