from os import read
from models import Product, Category
from sqlalchemy.orm import Session
from sqlalchemy import or_
import csv

class ProductDAO():

    def create(self, db: Session, product: Product):
        category = db.query(Category).filter(Category.id == product.categories_id[0]).first()        
        product_db = Product(
            name=product.name,
            description=product.description,
            value=product.value,
            categories_id=category.id
        )
        db.add(product_db)
        db.commit()
        db.refresh(product_db)
        return product_db

    def update(self, db: Session, product: Product, id: int):
        values_to_update = {}
        for key, value in product.dict().items():
            if value:
                values_to_update[key] = value

        db.query(Product).filter(Product.id == id).update(
            values_to_update)
        
        db.commit()

        product_updated = db.query(Product).filter(Product.id == id).first()
        return product_updated

    def read(self, db: Session):
        products = db.query(Product).filter().all()
        return products
    
    def read_by(self, db: Session, filters: dict):

        products = db.query(Product).filter(
            or_(
                Product.name == filters["name"], 
                Product.description == filters["description"],
                Product.value == filters["value"],
                Product.categories_id == filters["categories_id"],                 
            )
        ).all()
        return products
    
    def delete(self, db: Session, id: int):
        deleted_product = db.query(Product).filter(Product.id == id).first()
        db.query(Product).filter(Product.id == id).delete()
        db.commit()
        return deleted_product

class CategoryDAO():

    def create_from_csv(self, db: Session, file):        
        with open(file, 'r') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            for collumn in reader:
               self.create(db, category_name=collumn['Nome'])

        categories = db.query(Category).all()
        return categories

    def create(self, db: Session, category_name: str):
        category_db = Category(name=category_name)
        db.add(category_db)
        db.commit()
        db.refresh(category_db)