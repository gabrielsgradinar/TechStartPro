from ..schemas import ProductCreate, ProductUpdate
from ..models import Category, Product
from ..dao import CategoryDAO, ProductDAO
from ..conftest import init_db
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

file = "../categorias.csv"

mock_csv_categories = [
    {'name': 'Category Test', 'id': 1},
    {'name': 'Móveis', 'id': 2},
    {'name': 'Decoração', 'id': 3}, 
    {'name': 'Celular', 'id': 4}, 
    {'name': 'Informática', 'id': 5}, 
    {'name': 'Brinquedos', 'id': 6}
]

mock_create_product = ProductCreate(
    name="Product Create DAO",
    description="Product description",
    value=5.3,
    categories_id=[1]
)

mock_update_product = ProductUpdate(
    name="Product Update DAO",
    value=21.5,
)


def test_category_dao_create_from_csv(init_db):
    category_dao = CategoryDAO().create_from_csv(db=init_db, file=file)
    assert type(category_dao) == list
    select_categories = init_db.query(Category).all()
    assert category_dao == select_categories

def test_category_dao_create(init_db):
    category_dao = CategoryDAO().create(init_db, category_name="Games")
    assert isinstance(category_dao, Category)

def test_category_dao_read(init_db):
    categories_dao = CategoryDAO().read(init_db)
    assert type(categories_dao) == list

    for category in categories_dao:
        assert isinstance(category, Category)

def test_product_dao_create(init_db):
    product_dao = ProductDAO().create(init_db, mock_create_product)
    assert product_dao
    assert isinstance(product_dao, Product)

def test_product_dao_read(init_db):
    products_dao = ProductDAO().read(init_db)
    assert type(products_dao) == list

    for product in products_dao:
        assert isinstance(product, Product)

def test_product_dao_update(init_db):
    product_dao = ProductDAO().update(init_db, mock_update_product, 1)

    assert product_dao
    assert isinstance(product_dao, Product)

def test_product_dao_delete(init_db):
    id = 1
    product_to_delete = init_db.query(Product).filter(Product.id == id).first()
    product_deleted = ProductDAO().delete(init_db, id)
    assert product_deleted
    assert isinstance(product_deleted, Product)
    assert product_deleted == product_to_delete


