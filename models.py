from sqlalchemy import Column, Integer, String
from db import Base
from pydantic import BaseModel
class BookCreate(BaseModel):
    title: str
    author: str
    publish_year: int
    price: int

class BookInResponse(BookCreate):
    id: int

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    publish_year = Column(Integer)
    price = Column(Integer)
