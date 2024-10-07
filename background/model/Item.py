from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer, Float
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
Session = sessionmaker()
class Item(Base):
    __tablename__ = "Item"

    id = Column(Integer, primary_key = True)
    name = Column(String(1000))
    image = Column(String(1000))
    price = Column(String(100))

    def __repr__(self):
        return f"{id}-{name}-{price}"

