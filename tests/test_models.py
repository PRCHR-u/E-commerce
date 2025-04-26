import pytest
from src.models import Product, Category, Smartphone, LawnGrass


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


class TestProduct:
    """Тесты для класса Product"""

    def test_product_initialization(self):
        """Проверка корректной инициализации объекта Product"""
        product = Product("Смартфон", "Современный смартфон", 29999.99, 5)

        assert product.name == "Смартфон"
        assert product.description == "Современный смартфон"
        assert product.price == 29999.99
        assert product.quantity == 5

    def test_product_negative_quantity(self):
        """Проверка валидации отрицательного количества"""
        with pytest.raises(ValueError, match="Quantity cannot be negative"):
            Product("Смартфон", "Современный смартфон", 29999.99, -5)

    def test_product_zero_values(self):
        """Проверка корректной инициализации с нулевыми значениями"""
        product = Product("Смартфон", "Современный смартфон", 10.0, 0)
        assert product.quantity == 0
        product.price = 0.0
        assert product.price == 10.0

    def test_product_different_values(self):
        """Проверка инициализации объекта Product с разными значениями"""
        product = Product("Ноутбук", "Мощный игровой ноутбук", 99999.99, 1)
        assert product.name == "Ноутбук"
        assert product.description == "Мощный игровой ноутбук"
        assert product.price == 99999.99
        assert product.quantity == 1

    def test_product_wrong_type_name(self):
        with pytest.raises(TypeError):
            Product(123, "Современный смартфон", 29999.99, 5)

    def test_product_wrong_type_description(self):
        with pytest.raises(TypeError):
            Product("Смартфон", 123, 29999.99, 5)

    def test_product_wrong_type_price(self):
        with pytest.raises(TypeError):
            Product("Смартфон", "Современный смартфон", "29999.99", 5)

    def test_product_wrong_type_quantity(self):
        with pytest.raises(TypeError):
            Product("Смартфон", "Современный смартфон", 29999.99, "5")

    def test_new_product(self) -> None:
        """Проверяет корректность работы метода new_product."""
        product_data = {
            "name": "Телевизор",
            "description": "Современный телевизор",
            "price": 50000.0,
            "quantity": 3,
        }
        product = Product.new_product(product_data)
        assert product.name == "Телевизор"
        assert product.description == "Современный телевизор"
        assert product.price == 50000.0
        assert product.quantity == 3

    def test_product_price_setter(self):
        """Проверяет корректность работы сеттера для цены."""
        product = Product("Test Product", "Test Description", 100.0, 10)
        product.price = 200.0
        assert product.price == 200.0
        product.price = 0
        assert product.price == 200.0

    def test_product_price_setter_wrong_type(self):
        """Проверяет корректность работы сеттера для цены with wrong type."""
        product = Product("Test Product", "Test Description", 100.0, 10)
        with pytest.raises(TypeError):
            product.price = "wrong type"

    def test_product_str(self):
        """Проверка строкового представления объекта Product."""
        product = Product("Смартфон", "Современный смартфон", 29999.99, 5)
        expected_str = "Смартфон, 29999.99 руб. Остаток: 5 шт."
        assert str(product) == expected_str

    def test_product_add(self):
        """Проверяет корректность работы метода __add__."""
        product1 = Product("Смартфон", "Современный смартфон", 100, 10)
        product2 = Product("Чехол", "Защитный чехол", 200, 2)
        assert product1 + product2 == 1400

    def test_product_add_wrong_type(self):
        """Проверяет корректность работы метода __add__ with wrong type"""
        product1 = Product(
            "Product 1",
            description="Test Description",
            price=100.0,
            quantity=10

        )
        product3 = Product(            
            "Product 3",
            description="Test Description",
            price=100.0,
            quantity=0,
        )
       
        assert (
            product1 + product3 == 1000
            ), "Sum of product1 and product3 must be 1000"
        with pytest.raises(
                TypeError,
                match=(
                    "Unsupported operand type for \\+: Product and int"
                )


        ):
            product1 + 10

    def test_category_add_wrong_type(self, category):
        """Проверяет корректность сложения разных типов"""

    def test_product_add_different_types(self):
        """
        Test that adding a Smartphone to a LawnGrass raises a
        TypeError.
        """
        smartphone = Smartphone(
            "Smartphone", "Desc", 100.0, 1, "High", "Model", 128, "Black"
        )
        lawn_grass = LawnGrass(
            "LawnGrass",
            "Desc", 100.0, 1,
            "USA",
            14,
            "Green"
        )
        smartphone2 = Smartphone(
            "Smartphone2", "Desc", 100.0, 1, "High", "Model", 128, "Black"
            )
        assert smartphone + smartphone2 == 200.0, (
            "Sum of smartphone and smartphone2 must be 200"
        )
        with pytest.raises(
            TypeError,
            match=("Unsupported operand type for \\+: " +
                   "Smartphone and LawnGrass")
        ):
            smartphone + lawn_grass


class TestSmartphone:
    """Tests for Smartphone class"""

    def test_smartphone_creation(self):
        """Test correct Smartphone creation"""
        smartphone = Smartphone(
            name="Test Smartphone",
            description="Test Smartphone Description",
            price=500.0,
            quantity=5,
            efficiency="High",
            model="Test Model",
            memory=128,
            color="Black",
        )
        assert smartphone.name == "Test Smartphone"
        assert smartphone.description == "Test Smartphone Description"
        assert smartphone.price == 500.0
        assert smartphone.quantity == 5
        assert smartphone.efficiency == "High"
        assert smartphone.model == "Test Model"
        assert smartphone.memory == 128
        assert smartphone.color == "Black"


class TestLawnGrass:
    """Tests for LawnGrass class."""

    pass


class TestCategory:
    """Тесты для класса Category."""

    def test_category_initialization(self):
        """Проверка корректной инициализации объекта Category"""
        category = Category("Электроника", "Все виды электроники")
        assert category.name == "Электроника"
        assert category.description == "Все виды электроники"
        assert category.products == ""
        assert Category.total_categories == 1
        assert Category.total_products == 0

    def test_category_with_products(self):
        """Проверка инициализации категории с продуктами"""
        products = [
            Product("Смартфон", "Современный смартфон", 29999.99, 5),

            Product("Планшет", "Планшет для работы", 19999.99, 3),
        ]
        category = Category("Электроника", "Все виды электроники", products)

        assert len(category._products) == 2
        assert Category.total_products == 2
        assert products[0] in category._products
        assert products[1] in category._products

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
        category = Category(
            "Электроника",
            "Все виды электроники",
        )
        # Adding products
        products = [
            Product(
                    f"Продукт {i}",
                    f"Описание {i}",
                    1000.0 * i,
                    i
                ) for i in range(3)
        ]

        for product in products:
            category.add_product(product)

        assert len(category._products) == 3
        assert Category.total_products == 3

        # Удаляем продукт
        category.remove_product(products[0])
        assert len(category._products) == 2
        assert Category.total_products == 2

    def test_multiple_categories_with_products(self):
        """Проверка работы с несколькими категориями и продуктами"""
        # Создаем категории
        category1 = Category("Электроника", "Все виды электроники")
        category2 = Category("Аксессуары", "Аксессуары для техники")

        product1 = Product("Смартфон", "Современный смартфон", 29999.99, 5)
        product2 = Product("Чехол", "Защитный чехол", 999.99, 10)

        category1.add_product(product1)
        category2.add_product(product2)

        # Проверяем счетчики
        assert Category.total_categories == 2
        assert Category.total_products == 2
        assert len(category1._products) == 1
        assert len(category2._products) == 1
        assert category1.products.count("\n") == 1
        assert category2.products.count("\n") == 1

    def test_category_add_wrong_type(self, category):
        """Проверка добавления в категорию объекта неправильного типа."""

    def test_category_add_product_already_in_category(self):
        """Проверка добавления продукта, который уже есть в категории"""
        category = Category("Электроника", "Все виды электроники")
        product = Product("Смартфон", "Современный смартфон", 29999.99, 5)
        category.add_product(product)
        category.add_product(product)
        assert category.products.count("\n") == 1
        assert Category.total_products == 1

    def test_category_remove_product_not_in_category(self):
        """Проверка удаления продукта, которого нет в категории"""
        category = Category("Электроника", "Все виды электроники")
        product1 = Product("Смартфон", "Современный смартфон", 29999.99, 5)
        product2 = Product("Планшет", "Планшет для работы", 19999.99, 3)
        category.add_product(product1)
        category.remove_product(product2)
        assert len(category._products) == 1
        assert Category.total_products == 1
        assert product2 not in category._products

    def test_category_str(self):
        """Проверка строкового представления объекта Category."""

        category = Category("Электроника", "Все виды электроники")
        expected_str = "Электроника, количество продуктов: 0 шт."
        assert str(category) == expected_str

    def test_category_wrong_type_name(self):
        with pytest.raises(TypeError):
            Category(123, "Все виды электроники")

    def test_category_wrong_type_description(self):
        with pytest.raises(TypeError):
            Category("Электроника", 123)

    def test_category_wrong_type_products(self):
        with pytest.raises(TypeError):
            Category("Электроника", "Все виды электроники", products=123)


@pytest.fixture
def category():
    return Category(
        name="Test Category",
        description="Test Description",
    )


def test_product_creation(product):
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0  # Access the price using the getter
    assert product.quantity == 10


def test_category_creation(category):
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert category.products == ""
    assert Category.total_categories == 1
    assert Category.total_products == 0


def test_category_add_product(category, product):
    category.add_product(product)
    assert len(category._products) == 1
    assert product in category._products
    assert Category.total_products == 1


def test_category_remove_product(category, product):
    category.add_product(product)
    category.remove_product(product)
    assert len(category._products) == 0
    assert product not in category._products
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
    assert Category.total_products == 2  # Ожидаем, что всего 2 продукта
    assert len(category1._products) == 1
    assert len(category2._products) == 1
