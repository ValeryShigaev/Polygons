from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.websockets import WebSocket

from db import point_manager as ptm
from db import poly_manager as pm
from db import sig
from routing.router import api_router
# from routing.endpoints.polygons import router
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


app.include_router(router=api_router)
