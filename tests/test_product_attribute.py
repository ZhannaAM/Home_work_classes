
import pytest



from src.product import Product


some_product = Product("corn", "vegetable", 100, 10)
one_more_product = Product("Apple","fruit", 150 , 15)




def test_new_product():
    new_product = Product.new_product({"name": "apple", "description": "fruit", "price": 180,
         "quantity": 15})
    assert str(new_product) == 'apple, 180 руб. Остаток: 15 шт.'


def test_price():
    assert some_product.price == 100


def test_price_setter():
    some_product.price = 150
    assert some_product.price == 150


def test_add():
    assert some_product + one_more_product == 3750


def test_quantity():
    assert some_product.quantity == 10