from typing import List
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")


@dataclass
class Category:
    name: str
    description: str
    products: List[Product] = None

    def __post_init__(self) -> None:
        if self.products is None:
            self.products = []

    def add_product(self, product: Product) -> None:
        if product not in self.products:
            self.products.append(product)

    def remove_product(self, product: Product) -> None:
        if product in self.products:
            self.products.remove(product) 