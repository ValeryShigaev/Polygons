from typing import Union

from fastapi import FastAPI

from sqlalchemy import select
from sqlalchemy.orm import Session
from db.engine import async_session
from serializers.serializers import PolygonResult

from models.models import Poly

app = FastAPI()


@app.get("/")
async def get_poly():
    async with async_session() as session:
        async with session.begin():
            statement = (select(Poly))
            q = await session.execute(statement)

    return {PolygonResult(q.scalars().first().id)}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
