import pytest

from src.category import Category
from src.product import Product, Smartphone, LawnGrass
from tests.test_product_attribute import some_product


@pytest.fixture
def product_apple():
    return Product("Apple", "red", 99.9, 1000)


@pytest.fixture
def category_fruit():
    return Category("fruits", "fruits from India", [some_product])


@pytest.fixture
def smartphone():
    return Smartphone('Крутой телефон', 'Очень крутой и красивый', 9999999,
                      1, 150000, 'XS PRO MAX 10000', 256, 'Небесная синева')





@pytest.fixture
def lawn_grass():
    return LawnGrass('Зеленая трава', 'Очень зеленая и сочная', 100, 10,
                     'Россия', '5 дней ', 'зеленый')