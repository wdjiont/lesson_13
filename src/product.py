class Product:
    name: str
    description: str
    price: float
    number_of_products: int

    def __init__(self, name, description, price, number_of_products):
        self.name = name
        self.description = description
        self.price = price
        self.number_of_products = number_of_products
