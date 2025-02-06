from src.category import Category
from src.product import Product
from tests.test_product_attribute import some_product

category_1 = Category("fruits", "fruits from India", [some_product])
new_product = Product("Apple","fruit", 150 , 15)


def test_category_product():
    assert category_1.products ==  ['corn, 100 руб. Остаток: 10 шт.']


def test_category_add_product():
    category_1.add_product(new_product)
    assert category_1.products == ['corn, 100 руб. Остаток: 10 шт.','Apple, 150 руб. Остаток: 15 шт.']


def test_quantity_count():
    assert category_1.quantity_count() == 25