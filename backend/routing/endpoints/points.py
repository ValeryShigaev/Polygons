""" Get all points(places) endpoint """


from fastapi import APIRouter
from db import point_manager as ptm
from serializers import points_to_geojson

router = APIRouter(
    tags=["Points"],
    prefix="/points",
)


@router.get("/places")
async def get_places():
    db_data = await ptm.get_places()
    return await points_to_geojson(db_data)
