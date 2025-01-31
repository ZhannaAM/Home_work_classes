
import pytest

from src.product import BaseProduct, Car, LawnGrass, Product, Smartphone


def test_products_init(product):
    product_1 = Product("tomato", "red tomato from Azerbaijan", 150, 10)

    assert product_1.name == "tomato"
    assert product_1.description == "red tomato from Azerbaijan"
    assert product_1.price == 150
    assert product_1.quantity == 10


def test_new_product():
    product_data = {"name": "Banana", "description": "Fresh yellow banana", "price": 0.5, "quantity": 20}
    product_add = Product.new_product(product_data)
    assert product_add.name == "Banana"
    assert product_add.description == "Fresh yellow banana"
    assert product_add.price == 0.5
    assert product_add.quantity == 20


def test_price_setter():
    product = Product("Orange", "Fresh orange", 1.5, 15)
    assert repr(product) == "Product('Orange', 'Fresh orange', 1.5, 15)"

    product.price = 3.0
    assert product.price == 3.0

    product.price = -3.0
    assert product.price == 3.0


def test_str():
    product = Product("Orange", "Fresh orange", 1.5, 15)
    expected_data = "Orange, 1.5 руб. Остаток: 15 шт."
    assert str(product) == expected_data


def test_print(capsys):
    product1 = Product("apples", "Fresh apples", 7.5, 15)
    product1.price = -10
    str(product1)

    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"


def test_add():
    product = Product("Orange", "Fresh orange", 20, 5)
    product1 = Product("apples", "Fresh apples", 10, 15)
    assert product + product1 == 250

    product1 = Product("apples", "Fresh apples", -7.5, 15)
    str(product1)


def test_smartphone():
    product_phone_1 = Smartphone("xiaomi", "xiaomi 8gb", 500, 20, "Good", "note 8 pro", "128 gb", "blue")
    assert product_phone_1.name == "xiaomi"
    assert product_phone_1.description == "xiaomi 8gb"
    assert product_phone_1.price == 500
    assert product_phone_1.efficiency == "Good"
    assert product_phone_1.model == "note 8 pro"
    assert product_phone_1.memory == "128 gb"
    assert product_phone_1.color == "blue"


def test_phone_add():
    product_phone_1 = Smartphone("xiaomi", "xiaomi 8gb", 500, 20, "Good", "note 8 pro", "128 gb", "blue")
    product_phone_2 = Smartphone("infinix", "infinix 128/8", 700, 30, "Good", "Note 30", "128 gb", "Green")
    assert product_phone_1 + product_phone_2 == 1200

    with pytest.raises(TypeError):
        product_phone_1 + 1


def test_lawngrass():
    product_lawngrass_1 = LawnGrass("grass", "green grass", 800, 20, "Russia", "2 month", "green")
    assert product_lawngrass_1.name == "grass"
    assert product_lawngrass_1.description == "green grass"
    assert product_lawngrass_1.price == 800
    assert product_lawngrass_1.country == "Russia"
    assert product_lawngrass_1.germination_period == "2 month"
    assert product_lawngrass_1.color == "green"


def test_lawngrass_add():
    product_lawngrass_1 = LawnGrass("grass", "green grass", 800, 20, "Russia", "2 month", "green")
    product_lawngrass_2 = LawnGrass("grass", "blue grass", 1000, 5, "China", "2 month", "green")
    assert product_lawngrass_1 + product_lawngrass_2 == 1800

    with pytest.raises(TypeError):
        product_lawngrass_1 + 1


def test_car():
    product_car_1 = Car("BMW", 10000, 5, "black")
    assert product_car_1.name == "BMW"
    assert product_car_1.price == 10000
    assert product_car_1.quantity == 5
    assert product_car_1.color == "black"


def test_mixin_product(capsys):
    Product("apples", "Fresh apples", 7.5, 15)

    message = capsys.readouterr()
    assert message.out.strip() == "Product('apples', 'Fresh apples', 7.5, 15)"


def test_base_product():
    class Employee(BaseProduct):

        def __init__(self, name, surname, pay):
            self._name = name
            self.__surname = surname
            self.pay = pay

        def __add__(self, other):
            return self.pay + other.pay

    emp_1 = Employee("Ivan", "Ivanov", 50_000)
    emp_2 = Employee("Nurlan", "Grachev", 100_000)

    assert emp_1 + emp_2 == 150_000


def test_raise():
    with pytest.raises(ValueError):
        product_1 = Product("cucumber", "cucumber from Azerbaijan", 100, 0)  # noqa F841

def test_product(product):
    assert product.name == "55\" QLED 4K"
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.quantity == 7

