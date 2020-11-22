import pytest
from models import Category, Product
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from ..database import Base, engine
from ..main import app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./olist.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:        
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture(autouse=True)
def init_db():
    db = TestingSessionLocal()

    db.query(Category).delete()
    db.query(Product).delete()

    product = Product(
        name='Product',
        description='Product Description',
        value=17.5,
        categories_id=1,
    )
    category = Category(name="Games")
    db.add(product)
    db.add(category)
    db.commit()
    db.refresh(product)
    db.refresh(category)

    yield db

    db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

mock_csv_response = [
    {'name': 'Games', 'id': 1},
    {'name': 'Móveis', 'id': 2},
    {'name': 'Decoração', 'id': 3}, 
    {'name': 'Celular', 'id': 4}, 
    {'name': 'Informática', 'id': 5}, 
    {'name': 'Brinquedos', 'id': 6}
]

mock_create_product = {
    "name":"Product Create",
    "description":"Product description",
    "value":5.3,
    "categories_id":[1]
}

mock_error_create_product = {
    "name":"Product Create",
    "description":"Product description",
    "value":5.3,
    "categories_id":[0]
}

mock_update_product = {
    "name":"Product Update",
    "value":22.5,
}


def test_insert_categories_from_csv_file():
    response = client.get("/category/file")

    assert response.status_code == 200
    assert response.json() == mock_csv_response

def test_select_all_categories_with_api():
    response = client.get("/categories/")

    assert response.status_code == 200
    assert response.json()[0] == {'name': 'Games', 'id': 1}

def test_create_product_with_api():
    response = client.post('/product/', json=mock_create_product)

    mock_create_product['id'] = 2
    mock_create_product['categories_id'] = 1

    assert response.status_code == 200
    assert response.json() == mock_create_product

def test_error_create_product_with_api():
    response = client.post('/product/', json=mock_error_create_product)

    assert response.json() == {'error': 'Category ID does not exists'}

def test_update_product_with_api():   
    response = client.put('/product/1', json=mock_update_product)

    assert response.status_code == 200

def test_delete_product_with_api():
    response = client.delete('/product/1')

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name":"Product",
        "description":"Product Description",
        "value":17.5,
        "categories_id":1
    }

def test_select_all_products_with_api():
    response = client.get("/products/")

    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "name":"Product",
        "description":"Product Description",
        "value":17.5,
        "categories_id":1
    }]
