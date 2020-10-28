import pytest
from ..models import Product, Category
from starlette.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..database import Base
from ..main import app, get_db


SQL_DATABASE_URL = "sqlite:///./test_olist.db"

engine = create_engine(
    SQL_DATABASE_URL
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@pytest.fixture(autouse=True)
def init_db():
    db = TestingSessionLocal()

    # Clean up tables before importing the initial data
    db.query(Product).delete()
    db.query(Category).delete()
    db.commit()

    # Insert some data to start tests
    category = Category(name="Category Test")
    product = Product( 
        name="Product",
        description="Product description",
        value=17.50,
        categories_id=1
    )
    
    db.add(category)
    db.add(product)

    db.commit()
    db.refresh(category)
    db.refresh(product)

    yield db

    db.close() # close session after running the test
    
