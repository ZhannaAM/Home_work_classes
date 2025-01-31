import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product():
    return Product("onion", "green onion from grandmom`s garden", 35, 10)


@pytest.fixture
def category_1():
    return Category("shoes", "winter shoes", ["boots with fur", "winter jacket"])


@pytest.fixture
def init_category():
    category_1 = Category("products", "products for salad", [])
    return category_1


@pytest.fixture
def product_for_add():
    product_3 = Product("lettuce", "fresh lettuce", 50, 15)
    return product_3