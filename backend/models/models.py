from sqlalchemy import Column, Integer, Date, Float

from geoalchemy2 import Geometry

from db.engine import Base


class Poly(Base):
    __tablename__ = "poly"

    id = Column(Integer, primary_key=True)
    geom = Column(Geometry("POLYGON"))
