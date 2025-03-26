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
