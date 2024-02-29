class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, name, description, price, quantity):
        """
        Cоздает товар и возвращает объект,
        который можно добавлять в список товаров
        """
        return cls(name, description, price, quantity)

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

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity

