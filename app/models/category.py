from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Session
from app.db import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    product = relationship("Product", back_populates="categories")

    def insert_from_csv(self, db: Session, file):
        pass

