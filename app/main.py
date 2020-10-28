from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import Category
from dao import ProductDAO
from database import Base, engine, SessionLocal
import schemas
app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello Olist !!!"}

# CRUD PRODUTOS
@app.post("/product/")
async def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return ProductDAO().create(db=db, product=product)

@app.put("/product/{product_id}")
async def get_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    return ProductDAO().update(db=db, product=product, id=product_id)

@app.get("/product/")
async def get_product(db: Session = Depends(get_db)):
    return ProductDAO().read(db=db)

@app.delete("/product/{product_id}")
async def get_product(product_id : int, db: Session = Depends(get_db)):
    return ProductDAO().delete(db=db, id=product_id)


@app.get("/category/")
async def create_category(db: Session = Depends(get_db)):
    db_category = Category(name="Teste")
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


