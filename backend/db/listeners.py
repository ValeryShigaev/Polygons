import asyncio

from sqlalchemy import event
from models.models import Poly

sig = asyncio.Event()


@event.listens_for(Poly, "after_update")
def after_update_function(mapper, connection, target):
    sig.set()
