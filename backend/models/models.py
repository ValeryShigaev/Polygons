from sqlalchemy import Column, Integer, Date, Float

from sqlalchemy.orm import declarative_base

from geoalchemy2.types import Geometry

base = declarative_base()


class Poly(base):
    __tablename__ = "poly"

    id = Column(Integer, primary_key=True)
    geom = Column(Geometry("POLYGON", 4326))
