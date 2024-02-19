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
            result += f'{i.name}, {i.price} руб. Остаток: {i.number_of_products} шт.'
        return result

    @property
    def get_list(self):
        return self.__products


# cat_1 = Category('Lime', 'Магазин мужской одежды', [])
# pr_1 = Product('Футболка', 'хлопковая футболка', 2190.5, 13)
# pr_2 = Product('Шапка', 'теплая', 215, 1)
# pr_3 = Product('Брюки', 'джинсы', 3700, 5)
# cat_1.add_product(pr_1)
# cat_1.add_product(pr_2)
# cat_1.add_product(pr_3)
#
# print(cat_1.product_list)

