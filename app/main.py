from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.responses import Response
from dao import ProductDAO, CategoryDAO
from database import Base, engine, SessionLocal
from schemas import *
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
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return ProductDAO().create(db=db, product=product)
    
@app.get("/products/")
async def get_products(db: Session = Depends(get_db)):
    return ProductDAO().read(db=db)

@app.get("/product/")
async def get_product_by(
    db: Session = Depends(get_db), 
    name: str = "", 
    description: str = "",
    value: float = 0,
    categories_id: int = 0
):
    filters = {}
    if name: 
        filters["name"] = name
    if description: 
        filters["description"] = description
    if value:
        filters["value"] = value
    if categories_id:
        filters["categories_id"] = categories_id

    return ProductDAO().read_by(db=db, filters=filters)

@app.put("/product/{product_id}")
async def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    return ProductDAO().update(db=db, product=product, id=product_id)

@app.delete("/product/{product_id}")
async def delete_product(product_id : int, db: Session = Depends(get_db)):
    return ProductDAO().delete(db=db, id=product_id)

@app.get("/category/file")
async def create_category_from_file(db: Session = Depends(get_db)):
    file = "../categorias.csv"
    return CategoryDAO().create_from_csv(db=db, file=file)

@app.get("/categories/")
async def get_product_by(db: Session = Depends(get_db)):
    return CategoryDAO().read(db=db)
    


