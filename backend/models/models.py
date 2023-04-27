from sqlalchemy import Column, Integer, Date, Float, String

from sqlalchemy.orm import declarative_base

from geoalchemy2.types import Geometry

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
