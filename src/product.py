
from abc import ABC, abstractmethod


class BaseProduct(ABC):
     @abstractmethod
     def __init__(self):
         pass


class MixinParam:
    def __init__(self,name, description, price, quantity):
        super().__init__(name, description, price, quantity)
    def __repr__(self):
        return f'Product({self.name}, {self.description}, {self.price}, {self.quantity})'


class Product(BaseProduct, MixinParam):


class Product:


    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        super().__init__()
        if quantity <= 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')




    @classmethod
    def new_product(cls, product):
        name = product['name']
        description =product['description']
        price = product['price']
        quantity = product['quantity']
        return cls(name, description, price, quantity)


    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, new_price):
        if new_price == 0 or new_price < 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            self.__price = new_price


    def __add__(self,other):
        if type(self) == type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError


    def quantity(self):
        return self.quantity


class Smartphone(Product):
    efficiency: int
    model: str
    memory: int
    color: str
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color