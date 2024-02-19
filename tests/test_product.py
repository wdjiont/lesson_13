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


def test_create_product():
    new_product = Product.create_product('шапка', 'теплая', 215, 1)
    assert new_product.name == 'шапка'
    assert new_product.description == 'теплая'
    assert new_product.price == 215
    assert new_product.number_of_products == 1


def test_price(product):
    assert product.price == 2190.5


def test_another_price(product):
    product.price = 3000
    assert product.price == 3000
