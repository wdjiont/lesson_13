class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity, colour):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        self.colour = colour

    @classmethod
    def create_product(cls, name, description, price, quantity, colour):
        """
        Cоздает товар и возвращает объект,
        который можно добавлять в список товаров
        """
        return cls(name, description, price, quantity, colour)

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
        """Добавляет строковое отображение"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Складывает объекты между собой определенным методом"""
        if isinstance(other, type(self)):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, colour, productivity, model, memory):
        super().__init__(name, description, price, quantity, colour)
        self.productivity = productivity
        self.model = model
        self.memory = memory


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, colour, producing_country, germination_period):
        super().__init__(name, description, price, quantity, colour)
        self.producing_country = producing_country
        self.germination_period = germination_period


