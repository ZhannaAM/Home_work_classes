from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        self.product_count += len(products)
        Category.category_count += 1

    @property
    def products(self):
        product_list = []
        for product in self.__products:
            product_list.append(Product.__str__(product))
        return product_list


    def add_product(self,product):
        if isinstance(product, Product) is True:
            self.__products.append(product)
            self.product_count = len(self.__products)
            return self.__products
        else:
            raise TypeError


    def __str__(self):
        return f'{self.name}, количество продуктов: {self.quantity_count()}'


    def quantity_count(self):
        quantity_list = []
        for product in self.__products:
            quantity_list.append(Product.quantity(product))
        return sum(quantity_list)