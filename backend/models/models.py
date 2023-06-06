from geoalchemy2.types import Geometry
from sqlalchemy import Column, Date, Float, Integer, String
from sqlalchemy.orm import declarative_base

base = declarative_base()


class Poly(base):
    __tablename__ = "poly"

    id = Column(Integer, primary_key=True)
    geom = Column(Geometry("POLYGON", 4326))


class Places(base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True)
    geom = Column(Geometry("POINT", 4326))
    name = Column(String)
    pop_max = Column(Integer)
    featurecla = Column(String)
