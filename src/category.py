from abc import ABC, abstractmethod

from src.product import Product


class NoProducts(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Error"

    def __str__(self):
        return self.message


class Abstract(ABC):
    @abstractmethod
    def __repr__(self):
        pass


class Order(Abstract):
    def __init__(self, product, buy_count):
        self.product = product
        self.buy_count = buy_count
        self.total_price = self.buy_count * product.price

    def __repr__(self):
        return f"{self.product.name}, куплено - {self.buy_count} штук, итоговая стоимость - {self.total_price} рублей"


class Category(Abstract):
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        Category.category_count += 1
        Category.product_count += len(products)
        self.name = name
        self.description = description
        self.__products = products

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}')"

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    def add_product(self, product):
        # try:
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Нельзя добавлять разные классы")

    @property
    def products(self):
        return [
            f"Название продукта : {product.name}, цена : {product.price} рублей, Остаток: {product.quantity} штук."
            for product in self.__products
        ]

    @products.setter
    def products(self, new_products):
        self.__products = new_products

    def middle_price(self):
        try:
            return sum([product.price for product in self.__products]) // len(self.__products)
        except ZeroDivisionError:
            return 0


class Sort:
    def __init__(self, product_of_category):
        self.product = product_of_category
        self.index = 0

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        if self.index == len(self.product) - 1:
            raise StopIteration
        else:
            self.index += 1
            return self.product[self.index]


if __name__ == "__main__":
    try:
        product_1 = Product("tomato", "red tomato from Azerbaijan", 150, 10)
        category_1 = Category("products", "products for salad", [])
        category_1.add_product(product_1)
    except ValueError:
        try:
            raise NoProducts
        except NoProducts as e:
            print(e)
            print("Кол-во товара не может быть равным нулю")
    else:
        print("Товар добавлен в category")
    finally:
        print("Операция добавления закончена")