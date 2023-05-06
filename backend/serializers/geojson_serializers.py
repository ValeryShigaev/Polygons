from .base import GeojsonBase


class Serializer(GeojsonBase):

    async def serialize(self, *args):
        return await super().serialize(*args)
