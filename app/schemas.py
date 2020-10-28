from typing import List, Optional

from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = ""
    value: int
    categories_id: List


class ProductCreate(ProductBase):
    name: str
    description: Optional[str] = ""
    value: int
    categories_id: List


class ProductUpdate(ProductBase):
    name: Optional[str]
    description: Optional[str] = ""
    value: Optional[int]
    categories_id: Optional[List]



class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True