""" Database manager class that is responsible for working with points """

from sqlalchemy import select
from sqlalchemy.engine.result import ScalarResult

from models.models import Places

from .base import BaseManager


class PointManager(BaseManager):
    """
    Class that is responsible for working with points
    Parent: BaseManager
    Methods:
        get_places: this method allows to get points from database
    """

    async def get_places(self, indexes: list[int] = None) -> ScalarResult:
        """
        This method allows to get points from database. If the "indices"
        parameter is passed, then points with id will be given in accordance
        with the list

        :param indexes: list of necessary indexes
        :type indexes: list[int]
        :rtype: ScalarResult
        """

        async with self.async_session() as session:
            async with session.begin():
                if indexes:
                    indexes = tuple(indexes)
                    statement = (select(Places).where(Places.id.in_(indexes)))
                else:
                    statement = (select(Places).order_by(Places.id))
                points = await session.execute(statement)
        return points.scalars()

