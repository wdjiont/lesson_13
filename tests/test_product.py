import pytest

from src.product import Product


@pytest.fixture
def product():
    return Product('футболка', 'хлопковая футболка', 2190.5, 13)


def test_init_(product):
    assert product.name == 'футболка'
    assert product.description == 'хлопковая футболка'
    assert product.price == 2190.5
    assert product.number_of_products == 13
