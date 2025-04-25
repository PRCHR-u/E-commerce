from typing import List


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(description, str):
            raise TypeError("Description must be a string")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product_data):
        """Создает новый объект Product из словаря."""
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]
        return cls(name, description, price, quantity)

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


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: List[Product] = None) -> None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(description, str):
            raise TypeError("Description must be a string")
        if products is not None and not isinstance(products, list):
            raise TypeError("Products must be a list or None")

        self.name = name
        self.description = description
        self._products: List[Product] = []
        if products:
            for product in products:
                self.add_product(product)

        Category.total_categories += 1

    def add_product(self, product: Product) -> None:
        if product not in self._products:
            self._products.append(product)
            Category.total_products += 1

    def remove_product(self, product: Product) -> None:
        if product in self._products:
            self._products.remove(product)
            Category.total_products -= 1

    @property
    def products(self) -> str:
        products_info = ""
        for product in self._products:
            products_info += str(product) + "\n"
        return products_info