class Product:
    name: str
    description: str
    price: float
    number_of_products: int

    def __init__(self, name, description, price, number_of_products):
        self.name = name
        self.description = description
        self._price = price
        self.number_of_products = number_of_products

    @classmethod
    def create_product(cls, name, description, price, number_of_products):
        """
        Cоздает товар и возвращает объект,
        который можно добавлять в список товаров
        """
        return cls(name, description, price, number_of_products)

    @property
    def price(self):
        """Возвращает стоимость товара"""
        return self._price

    @price.setter
    def price(self, new_price):
        """Принимает на вход новую стоимость и устанавливает ее вместо старой"""
        if new_price <= 0:
            print('Цена введена некорректно')
        elif new_price < self._price:
            user_price = input('Если вы действительно хотите изменить цену: введите "y" \nЕсли хотите оставить цену прежней: введите "n"\n')
            if user_price == "y":
                self._price = new_price
            elif user_price != "n" and user_price != "y":
                print("Некорректный ввод, попробуйте снова")
        else:
            self._price = new_price


# pr_1 = Product('футболка', 'хлопковая футболка', 2190.5, 13)
# pr_1.price
# print(pr_1.price)
# print(pr_1.price)
# pr_1.price = 4000
# print(pr_1.price)
# cat_1.add_product(pr_1)
# pr_2 = Product('шапка', 'теплая', 215, 1)
# pr_3 = Product('брюки', 'джинсы', 3700, 5)
# cat_1.add_product(pr_2)
# cat_1.add_product(pr_3)
# # new_pr = Product.product_make('шапка', 'блаблабла', 150, 12, cat_1.products)
# new_p = Product.product_make('шапка', 'блаблабла', 130, 10, cat_1.get_list)
# print(new_p.price)

