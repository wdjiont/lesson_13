import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def category_shop():
    return Category('Lime', 'Магазин мужской одежды', [])


def test_init(category_shop):
    assert category_shop.name == 'Lime'
    assert category_shop.description == 'Магазин мужской одежды'
    assert Category.category_count == 2
    assert Category.product_count == 0


def test_add_product(category_shop):
    pr_1 = Product('Футболка', 'хлопковая футболка', 2190.5, 13)
    assert category_shop.add_product(pr_1.name) == ['Футболка']


def test_product_list(category_shop):
    pr_1 = Product('Футболка', 'хлопковая футболка', 2190.5, 13)
    category_shop.add_product(pr_1)
    assert category_shop.product_list == "Футболка, 2190.5 руб. Остаток: 13 шт."


def test_len(category_shop):
    pr_1 = Product('Футболка', 'хлопковая футболка', 2190.5, 13)
    category_shop.add_product(pr_1)
    assert len(category_shop) == 13


def test_str(category_shop):
    pr_1 = Product('Футболка', 'хлопковая футболка', 2190.5, 13)
    category_shop.add_product(pr_1)
    assert category_shop.__str__() == "Lime, количество продуктов: 13 шт."
