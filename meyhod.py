"""
    Extend the Product class to include a method that calculates the total cost of a
    certain quantity of that product. 
"""

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

    def calculate_total_cost_for_quantity(self, quantity):
        return self.price * quantity


apple_product = Product(name='banana', price=4.0, quantity=7)


print(f"Product Name: {apple_product.name}")
print(f"Price per unit: ${apple_product.price}")
print(f"Quantity: {apple_product.quantity}")
print(f"Total Cost for 7 units: ${apple_product.calculate_total():.2f}")


quantity_to_calculate = 4
total_cost_for_quantity = apple_product.calculate_total_cost_for_quantity(quantity_to_calculate)
print(f"Total Cost for {quantity_to_calculate} units: ${total_cost_for_quantity:.2f}")

