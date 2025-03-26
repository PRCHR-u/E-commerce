# E-commerce Project

Проект для управления электронной коммерцией с классами Product и Category.

## Установка

1. Убедитесь, что у вас установлен Poetry
2. Клонируйте репозиторий
3. Установите зависимости:
```bash
poetry install
```

## Структура проекта

```
e-commerce/
├── src/
│   ├── __init__.py
│   └── models.py
├── tests/
├── pyproject.toml
└── README.md
```

## Использование

```python
from src.models import Product, Category

# Создание продукта
product = Product(
    name="Телефон",
    description="Смартфон последнего поколения",
    price=999.99,
    quantity=10
)

# Создание категории
category = Category(
    name="Электроника",
    description="Все виды электронных устройств",
    products=[product]
)
```

## Разработка

Проект использует следующие инструменты для обеспечения качества кода:
- Black для форматирования
- Flake8 для проверки стиля
- MyPy для статической типизации
- Pytest для тестирования 