from typing import List
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str,
                 price: float, quantity: int) -> None:        
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(description, str):
            raise TypeError("Description must be a string")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity




        if self.price < 0:
            raise ValueError("Price cannot be negative")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str,
                 products: List[Product] = None) -> None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(description, str):
            raise TypeError("Description must be a string")
        if products is not None and not isinstance(products, list):
            raise TypeError("Products must be a list or None")
        self.name = name
        self.description = description
        self.products = products if products is not None else []
        Category.total_categories += 1
        Category.total_products += len(self.products)

    @property
    def category_count(self):
        return Category.total_categories

    @property
    def product_count(self):
        return len(self.products)

    def add_product(self, product: Product) -> None:
        if product not in self.products:
            self.products.append(product)
            Category.total_products += 1

    def remove_product(self, product: Product) -> None:
        if product in self.products:
            self.products.remove(product)
            Category.total_products -= 1
