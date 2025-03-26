import pytest
from src.models import Product, Category


@pytest.fixture
def product():
    return Product(
        name="Test Product",
        description="Test Description",
        price=100.0,
        quantity=10,
    )


@pytest.fixture
def category():
    return Category(
        name="Test Category",
        description="Test Description",
    )


def test_product_creation(product):
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_negative_price():
    with pytest.raises(ValueError, match="Price cannot be negative"):
        Product(
            name="Test Product",
            description="Test Description",
            price=-100.0,
            quantity=10,
        )


def test_product_negative_quantity():
    with pytest.raises(ValueError, match="Quantity cannot be negative"):
        Product(
            name="Test Product",
            description="Test Description",
            price=100.0,
            quantity=-10,
        )


def test_category_creation(category):
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert category.products == []


def test_category_add_product(category, product):
    category.add_product(product)
    assert len(category.products) == 1
    assert product in category.products


def test_category_remove_product(category, product):
    category.add_product(product)
    category.remove_product(product)
    assert len(category.products) == 0
    assert product not in category.products 