from abc import ABC, abstractmethod
from typing import List, Union


class ReprMixin:
    def __init__(self, *args, **kwargs):
        pass

    def __repr__(self):
        attributes = self.__dict__
        name = attributes.get("name")
        description = attributes.get("description")
        price = attributes.get("_price")
        quantity = attributes.get("quantity")
        return (
            f"{self.__class__.__name__}(name={repr(name)}, "
            f"description={repr(description)}, "
            f"price={repr(price)}, quantity={repr(quantity)})"
        )


class BaseProduct(ABC):
    """
    Abstract base class for products.


    """

    @abstractmethod
    def __init__(
        self,
        name: str,
        description: str,
        price: Union[int, float],
        quantity: int,
    ) -> None:
        """Инициализация продукта."""
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def __add__(self, other):
        pass


class Product(ReprMixin, BaseProduct):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        """Инициализация продукта."""
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(description, str):
            raise TypeError("Description must be a string")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        ReprMixin.__init__(
            self,
            name=name,
            description=description,
            price=price,
            quantity=quantity
        )
        BaseProduct.__init__(self, name, description, price, quantity)

        self.price = price

    def __add__(self, other):
        """
        Сложение товаров.
        Складываются полные стоимости двух товаров.
        """
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"Unsupported operand type for +: "
                f"{self.__class__.__name__} and "
                f"{other.__class__.__name__}"
            )
        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        else:
            self._price = value

    def __str__(self):
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."


class Smartphone(Product):

    """Смартфон."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: str,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Инициализация смартфона."""
        Product.__init__(self, name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Трава газонная."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Инициализация травы газонной."""
        Product.__init__(self, name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    category_count = 0
    product_count = 0

    def __init__(
        self, name: str, description: str, products: List[Product] = None
    ) -> None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(description, str):
            raise TypeError("Description must be a string")
        if products is not None and not isinstance(products, list):
            raise TypeError("Products must be a list or None")

        self.name = name
        self.description = description
        self._products: List[Product] = []
        Category.category_count += 1
        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError(
                "The object must be a Product or a subclass of Product."
                )

        if product not in self._products:
            self._products.append(product)
            Category.product_count += 1

    def remove_product(self, product: Product) -> None:
        if product in self._products:
            self._products.remove(product)
            Category.product_count -= 1

        else:
            print("this product is not in category")

    @property
    def products(self) -> str:
        products_info = ""
        for product in self._products:
            products_info += str(product) + "\n"
        return products_info

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {len(self._products)} шт."
