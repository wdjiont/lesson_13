from src.product import Product


class Category:
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(set(products))

    def add_product(self, product):
        """
        Принимает на вход объект товара и добавляет в список
        """
        list_product = self.__products
        list_product.append(product)
        return list_product

    @property
    def product_list(self):
        """Возвращает список товаров в нужном формате"""
        result = ''
        for i in self.__products:
            result += f'{i.name}, {i.price} руб. Остаток: {i.quantity} шт.'
        return result

    @property
    def get_list(self):
        return self.__products

    def __len__(self):
        """Считает количество всех продуктов на складе"""
        all_products = 0
        for i in self.__products:
            all_products += i.quantity
        return all_products

    def __str__(self):
        """Добавляет строковое отображение"""
        return f"{self.name}, количество продуктов: {len(self)} шт."

