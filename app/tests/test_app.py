from os import ctermid
from ..models import Category, Product
from .conftest import client, init_db

mock_csv_response = [
    {'name': 'Category Test', 'id': 1},
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

mock_update_product = {
    "name":"Product Update",
    "value":22.5,
}


def test_insert_categories_from_csv_file(init_db):
    response = client.get("/category/file")

    assert response.status_code == 200
    assert response.json() == mock_csv_response

def test_select_all_categories_with_api(init_db):
    response = client.get("/categories/")

    assert response.status_code == 200
    assert response.json() == [{
        "id":1, 
        "name":"Category Test"
    }]

def test_create_product_with_api(init_db):
    response = client.post('/product/', json=mock_create_product)

    mock_create_product['id'] = 2
    mock_create_product['categories_id'] = 1

    assert response.status_code == 200
    assert response.json() == mock_create_product

def test_update_product_with_api(init_db):   
    response = client.put('/product/2', json=mock_update_product)

    assert response.status_code == 200

def test_delete_product_with_api(init_db):   
    response = client.delete('/product/1')

    assert response.status_code == 200
    assert response.json() == {
        'id': 1, 
        'value': 17.5, 
        'name': 'Product', 
        'categories_id': 1, 
        'description': 'Product description'
    }

def test_select_all_products_with_api(init_db):
    response = client.get("/products/")

    assert response.status_code == 200
    assert response.json() == [{
        'id': 1, 
        'value': 17.5, 
        'name': 'Product', 
        'categories_id': 1, 
        'description': 'Product description'
    }]

def test_select_products_using_filters_with_api(init_db):
    pass
