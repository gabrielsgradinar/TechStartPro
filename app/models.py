from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    Float, 
    ForeignKey,
)
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__ = 'products'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(String(250))
    value = Column(Float(asdecimal=True))
    categories_id = Column(Integer, ForeignKey("categories.id"))

    categories = relationship("Category", back_populates="products")

    def __repr__(self) -> str:
        return f"name = {self.name}"


class Category(Base):
    __tablename__ = 'categories'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))

    products = relationship("Product", back_populates="categories")

    def __repr__(self) -> str:
        return f"name = {self.name}"
