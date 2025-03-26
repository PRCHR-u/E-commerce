import pytest
from src.models import Product, Category
from typing import List


@pytest.fixture(autouse=True)
def reset_counters():
    """Сброс счетчиков перед каждым тестом"""
    Category.total_categories = 0
    Category.total_products = 0


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


class TestProduct:
    """Тесты для класса Product"""

    def test_product_initialization(self):
        """Проверка корректной инициализации объекта Product"""
        product = Product("Смартфон", "Современный смартфон", 29999.99, 5)

        assert product.name == "Смартфон"
        assert product.description == "Современный смартфон"
        assert product.price == 29999.99
        assert product.quantity == 5

    def test_product_negative_price(self):
        """Проверка валидации отрицательной цены"""
        with pytest.raises(ValueError, match="Price cannot be negative"):
            Product("Смартфон", "Современный смартфон", -29999.99, 5)

    def test_product_negative_quantity(self):
        """Проверка валидации отрицательного количества"""
        with pytest.raises(ValueError, match="Quantity cannot be negative"):
            Product("Смартфон", "Современный смартфон", 29999.99, -5)

    def test_product_zero_values(self):
        """Проверка корректной инициализации с нулевыми значениями"""
        product = Product("Смартфон", "Современный смартфон", 0.0, 0)

        assert product.price == 0.0
        assert product.quantity == 0


class TestCategory:
    """Тесты для класса Category"""

    def test_category_initialization(self):
        """Проверка корректной инициализации объекта Category"""
        category = Category("Электроника", "Все виды электроники")

        assert category.name == "Электроника"
        assert category.description == "Все виды электроники"
        assert category.products == []
        assert Category.total_categories == 1
        assert Category.total_products == 0

    def test_category_with_products(self):
        """Проверка инициализации категории с продуктами"""
        products = [
            Product("Смартфон", "Современный смартфон", 29999.99, 5),
            Product("Планшет", "Планшет для работы", 19999.99, 3)
        ]
        category = Category("Электроника", "Все виды электроники", products)

        assert len(category.products) == 2
        assert Category.total_products == 2
        assert products[0] in category.products
        assert products[1] in category.products

    def test_category_counting(self):
        """Проверка подсчета количества категорий"""
        # Создаем несколько категорий
        categories = [
            Category(f"Категория {i}", f"Описание {i}")
            for i in range(3)
        ]

        assert Category.total_categories == 3
        assert len(categories) == 3

    def test_product_counting(self):
        """Проверка подсчета количества продуктов"""
        category = Category("Электроника", "Все виды электроники")

        # Добавляем продукты
        products = [
            Product(f"Продукт {i}", f"Описание {i}", 1000.0 * i, i)
            for i in range(3)
        ]

        for product in products:
            category.add_product(product)

        assert len(category.products) == 3
        assert Category.total_products == 3

        # Удаляем продукт
        category.remove_product(products[0])
        assert len(category.products) == 2
        assert Category.total_products == 2

    def test_multiple_categories_with_products(self):
        """Проверка работы с несколькими категориями и продуктами"""
        # Создаем категории
        category1 = Category("Электроника", "Все виды электроники")
        category2 = Category("Аксессуары", "Аксессуары для техники")

        # Создаем продукты
        product1 = Product("Смартфон", "Современный смартфон", 29999.99, 5)
        product2 = Product("Чехол", "Защитный чехол", 999.99, 10)

        # Добавляем продукты в категории
        category1.add_product(product1)
        category2.add_product(product2)

        # Проверяем счетчики
        assert Category.total_categories == 2  # Ожидаем, что всего 2 категории
        assert Category.total_products == 2     # Ожидаем, что всего 2 продукта
        assert len(category1.products) == 1
        assert len(category2.products) == 1


def test_product_creation(product):
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_category_creation(category):
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert category.products == []
    assert Category.total_categories == 1
    assert Category.total_products == 0


def test_category_add_product(category, product):
    category.add_product(product)
    assert len(category.products) == 1
    assert product in category.products
    assert Category.total_products == 1


def test_category_remove_product(category, product):
    category.add_product(product)
    category.remove_product(product)
    assert len(category.products) == 0
    assert product not in category.products
    assert Category.total_products == 0


def test_multiple_categories():
    """Проверка работы с несколькими категориями и продуктами"""
    # Создаем категории
    category1 = Category("Электроника", "Все виды электроники")
    category2 = Category("Аксессуары", "Аксессуары для техники")

    # Создаем продукты
    product1 = Product("Смартфон", "Современный смартфон", 29999.99, 5)
    product2 = Product("Чехол", "Защитный чехол", 999.99, 10)

    # Добавляем продукты в категории
    category1.add_product(product1)
    category2.add_product(product2)

    # Проверяем счетчики
    assert Category.total_categories == 2  # Ожидаем, что всего 2 категории
    assert Category.total_products == 2     # Ожидаем, что всего 2 продукта
    assert len(category1.products) == 1     # В первой категории 1 продукт
    assert len(category2.products) == 1     # Во второй категории 1 продукт


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

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию и увеличивает счетчик продуктов."""
        if product not in self.products:
            self.products.append(product)
            Category.total_products += 1

    def remove_product(self, product: Product) -> None:
        """Удаляет продукт из категории и уменьшает счетчик продуктов."""
        if product in self.products:
            self.products.remove(product)
            Category.total_products -= 1  # Уменьшаем счетчик продуктов
