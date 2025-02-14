from tests.test_product_attribute import some_product


def test_init_product(product_apple):
    assert product_apple.name == "Apple"
    assert product_apple.description == "red"
    assert product_apple.price == 99.9
    assert product_apple.quantity == 1000
    assert product_apple.__repr__() == 'Product(Apple, red, 99.9, 1000)'


def test_init_category(category_fruit):
    assert category_fruit.name == "fruits"
    assert category_fruit.description == "fruits from India"
    assert category_fruit.products == [str(some_product)]
    assert category_fruit.product_count == 1
    assert category_fruit.category_count == 3


def test_init_Smartphone(smartphone):
    assert smartphone.name == 'Крутой телефон'
    assert smartphone.description == 'Очень крутой и красивый'
    assert smartphone.price == 9999999
    assert smartphone.quantity == 1
    assert smartphone.efficiency == 150000
    assert smartphone.model == 'XS PRO MAX 10000'
    assert smartphone.memory == 256
    assert smartphone.color == 'Небесная синева'


def test_init_lawn_grass(lawn_grass):
    assert lawn_grass.name == 'Зеленая трава'
    assert lawn_grass.description == 'Очень зеленая и сочная'
    assert lawn_grass.price == 100
    assert lawn_grass.quantity == 10
    assert lawn_grass.country == 'Россия'
    assert lawn_grass.germination_period == '5 дней '
    assert lawn_grass.color == 'зеленый'