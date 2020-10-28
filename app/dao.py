from models import Product, Category
from schemas import ProductCreate, ProductUpdate
from sqlalchemy.orm import Session
from sqlalchemy import or_
import csv

class ProductDAO():

    def create(self, db: Session, product: ProductCreate):
        category = db.query(Category).filter(Category.id == product.categories_id[0]).first()
        if not category:
            return {'error': 'Category ID does not exists'}   

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

    def update(self, db: Session, product: ProductUpdate, id: int):
        values_to_update = {}
        for key, value in product.dict().items():
            if value:
                values_to_update[key] = value

        db.query(Product).filter(Product.id == id).update(values_to_update)
        
        db.commit()

        product_updated = db.query(Product).filter(Product.id == id).first()
        return product_updated

    def read(self, db: Session):
        products = db.query(Product).filter().all()
        return products
    
    def read_by(self, db: Session, filters: dict):

        filter_query = self.create_filter(filters)

        print(*filter_query)

        # products = db.query(Product).filter(
        #     or_(
        #         *filter_query              
        #     )
        # ).all()
        # return products
    
    def delete(self, db: Session, id: int):
        deleted_product = db.query(Product).filter(Product.id == id).first()
        db.query(Product).filter(Product.id == id).delete()
        db.commit()
        return deleted_product

    def create_filter(self, filters):
        filter_query = []

        for key in filters.keys():
            if key == "name":
                filter_query.append(Product.name == filters[key])
            if key == "description":
                filter_query.append(Product.name == filters[key])
            if key == "value":
                filter_query.append(Product.name == filters[key])
            if key == "categories_id":
                filter_query.append(Product.name == filters[key])
        
        return filter_query

class CategoryDAO():

    def create_from_csv(self, db: Session, file):        
        with open(file, 'r') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            for collumn in reader:
               self.create(db, category_name=collumn['Nome'])

        categories = db.query(Category).all()
        return categories
    
    def read(self, db: Session):
        categories = db.query(Category).filter().all()
        return categories

    def create(self, db: Session, category_name: str):
        category_db = Category(name=category_name)
        db.add(category_db)
        db.commit()
        db.refresh(category_db)
        return category_db