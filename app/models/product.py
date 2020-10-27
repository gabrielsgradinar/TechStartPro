from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    Float, 
    ForeignKey
)
from sqlalchemy.orm import relationship
from app.db import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(String(250))
    value = Column(Float)
    categories_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="products")

