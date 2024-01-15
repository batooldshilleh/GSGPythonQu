"""
->   Define a class Product with attributes like name, price, and quantity. 
->    Create an instance of the class and showcase its usage. 
"""

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity


apple_product = Product(name='banana', price=4.0, quantity=7)


print(f"Product Name: {apple_product.name}")
print(f"Price per unit: ${apple_product.price}")
print(f"Quantity: {apple_product.quantity}")
print(f"Total Cost: ${apple_product.calculate_total():.2f}")

