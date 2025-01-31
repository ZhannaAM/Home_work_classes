
import pytest

from src.category import Category, NoProducts, Order, Sort
from src.product import Car, Product


def test_category(category_1, product, capsys):
    product1 = Product("boots with fur", 100, 10, 15)
    product2 = Product("winter jacket", 150, 5, 15)
    category = Category("shoes", "winter shoes", [product1, product2])

    assert category.name == "shoes"
    assert category.description == "winter shoes"
    assert category.category_count == 2
    assert category.product_count == 4
    assert repr(category) == f"Category('shoes', 'winter shoes')"  # noqa F541

    expected_product_1 = (
        f"Название продукта : {product1.name}, цена : {product1.price} рублей, Остаток: {product1.quantity} штук."
    )
    expected_product_2 = (
        f"Название продукта : {product2.name}, цена : {product2.price} рублей, Остаток: {product2.quantity} штук."
    )

    assert category.products[0] == expected_product_1
    assert category.products[1] == expected_product_2

    product3 = Product("summer dress", 100, 345, 25)
    category.add_product(product3)

    assert len(category.products) == 3
    assert "summer dress" in category.products[-1]

    product1 = Product("Товар1", 100, 10, 45)
    product2 = Product("Товар2", 200, 5, 46)
    category = Category("Электроника", "Различные электронные устройства", [product1, product2])
    expected_str = f"Электроника, количество продуктов: 2 шт."  # noqa F541
    assert str(category) == expected_str

    product_3 = Product("apples", "red apples from Azerbaijan", 200, 25)
    product_4 = Product("pears", "green pears from Azerbaijan", 250, 30)

    assert len(category.products) == 2
    category.products = [product_3, product_4]
    assert category.products[0] == "Название продукта : apples, цена : 200 рублей, Остаток: 25 штук."
    assert category.products[1] == "Название продукта : pears, цена : 250 рублей, Остаток: 30 штук."

    product_1 = Product("tomato", "red tomato from Azerbaijan", 150, 10)
    product_2 = Product("cucumber", "cucumber from Azerbaijan", 100, 20)
    cat = Sort([product_1, product_2])
    list_cat = list(cat)
    assert list_cat[0] == product_1
    assert list_cat[1] == product_2

    product_car_1 = Car("BMW", 10000, 5, "black")
    with pytest.raises(TypeError):
        category.add_product(product_car_1)
        message = capsys.readouterr()
        assert message.out.strip() == "Нельзя добавлять разные классы"

    product_1 = Product("tomato", "red tomato from Azerbaijan", 150, 10)
    order = Order(product_1, 20)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Product('tomato', 'red tomato from Azerbaijan', 150, 10)"
    assert repr(order) == "tomato, куплено - 20 штук, итоговая стоимость - 3000 рублей"

    category_1 = Category("products", "products for salad", [product_1, product_2])
    assert category_1.middle_price() == 125

    category_1 = Category("products", "products for salad", [])
    assert category_1.middle_price() == 0

    with pytest.raises(NoProducts):
        try:
            product_1 = Product("tomato", "red tomato from Azerbaijan", 150, 0)
            category_1 = Category("products", "products for salad", [])
            category_1.add_product(product_1)
        except ValueError:
            raise NoProducts

    with pytest.raises(NoProducts) as exc_info:
        raise NoProducts

    assert str(exc_info.value) == "Error"

def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(first_category.list_product) == 3

    assert first_category.category_count == 2
    assert second_category.product_count == 4
