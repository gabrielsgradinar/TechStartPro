from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    Float, 
    ForeignKey,
    Table
)
from sqlalchemy.orm import relationship
from database import Base


association_table = Table('association', Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(String(250))
    value = Column(Float(asdecimal=True))
    categories_id = Column(Integer, ForeignKey("categories.id"))

    categories = relationship("Category", back_populates="products")

    def __repr__(self) -> str:
        return f"Product -> name = {self.name}, description = {self.description}, value = {self.value} , categories_id= {self.categories_id}"


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))

    products = relationship("Product", back_populates="categories")

    def __repr__(self) -> str:
        return f"Category -> name = {self.name}"


