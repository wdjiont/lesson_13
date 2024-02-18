import pytest

from src.category import Category


@pytest.fixture
def category_shop():
    return Category('Lime', 'Магазин мужской одежды', ['футблка', 'брюки', 'рубашка', 'ремень'])


def test_init(category_shop):
    assert category_shop.name == 'Lime'
    assert category_shop.description == 'Магазин мужской одежды'
    assert category_shop.products == ['футблка', 'брюки', 'рубашка', 'ремень']
    assert Category.category_count == 1
    assert Category.product_count == 4
