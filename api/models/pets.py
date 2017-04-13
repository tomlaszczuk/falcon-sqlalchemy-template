from sqlalchemy import String, Integer, Column

from .base import Base


class Pet(Base):

    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
