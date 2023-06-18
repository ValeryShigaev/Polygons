""" Polygons endpoints """

import json
from fastapi import APIRouter, Depends
from starlette.websockets import WebSocket
from db import poly_manager as pm
from db import point_manager as ptm
from db import sig
from serializers import poly_to_geojson, inside_the_polygon, DataToUpdate

router = APIRouter(
    tags=["Polygons"],
    prefix="/polygons",
)


@router.get("/")
async def get_poly():
    """
    Returns all polygons

    :rtype: json
    """

    db_data = await pm.get_polygons()
    return await poly_to_geojson(db_data)


@router.get("/poly_info/{poly_id}")
async def poly_info(poly_id: int) -> dict:
    """
    Returns points(places) which are inside the polygon

    :param poly_id: inside which polygon
    :type poly_id: int
    :rtype: dict
    """

    poly_data = await pm.get_polygons(fid=poly_id)
    points_data = await ptm.get_places()
    return await inside_the_polygon(poly_data, points_data)


@router.post("/poly_update/")
async def poly_update(data: DataToUpdate = Depends()) -> bool:
    """
    To change the geometry of a polygon vertex

    data: incoming poly id, vertex id and new lat+lon
    :type data: DataToUpdate
    :rtype: bool
    """

    result = await pm.update_polygon(data.poly_id, data.vertex_id, data.latlng)
    return result


@router.websocket_route("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """ Websocket returns all polygons if db data changed """

    await websocket.accept()
    await websocket.send_json(await get_poly())
    while True:
        await sig.wait()
        if sig:
            await websocket.send_json(await get_poly())
            sig.clear()

