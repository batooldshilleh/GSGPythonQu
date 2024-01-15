"""
->    Implement a function that takes a dictionary of products and their prices.
->    Calculate the total cost of a given basket of products and apply a discount of 10%. Print
      the discounted total. 
"""

def calculate_discounted_total(basket, product_prices):
    total_cost = 0

    
    for product, quantity in basket.items():
        if product in product_prices:
            total_cost += quantity * product_prices[product]
        else:
            print(f"Warning: Product '{product}' not found in prices.")

  
    discounted_total = total_cost * 0.9

    return discounted_total


product_prices = {
    'apple': 1.0,
    'banana': 0.5,
    'orange': 1.2,
    'grape': 2.0
}


basket = {
    'apple': 3,
    'banana': 2,
    'orange': 1
}


discounted_total = calculate_discounted_total(basket, product_prices)
print(f"Discounted Total: ${discounted_total:.2f}")

