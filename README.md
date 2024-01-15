#  Technical Assessment: Python Proficiency

## Variable Types and Functional Programming: 
### Task 1: 
 **📑 Code Explanation**
```python
def calculate_sales_statistics(sales):
    total_sales = sum(sales)
    average_sales = total_sales / len(sales)
    return total_sales, average_sales
```
 function is to take a list of sales amounts, calculate the total sales, calculate the average sales, and return these values as a tuple.

 ```python
sales_week = [100, 150, 200, 120, 180, 250, 170]
```
Example list

 ```python
total_sales, average_sales = calculate_sales_statistics(sales_week)
```
Calculate total and average sales


 ```python
print("Total Sales: $", total_sales)
print("Average Sales: $", average_sales)
```
Print

**📊 Out Put**
```
Total Sales: $ 1170
Average Sales: $ 167.14285714285714
```

### Task 2: 
 **📑 Code Explanation**
```python
def calculate_discounted_total(basket, product_prices):
    total_cost = 0

    
    for product, quantity in basket.items():
        if product in product_prices:
            total_cost += quantity * product_prices[product]
        else:
            print(f"Warning: Product '{product}' not found in prices.")

  
    discounted_total = total_cost * 0.9

    return discounted_total
```
this function takes a dictionary (basket) representing a collection of products and their quantities, and another dictionary (product_prices) representing the prices of those products. It calculates the total cost of the items in the basket, applies a 10% discount, and returns the discounted total cost. The function also prints a warning for any product in the basket that is not found in the product_prices dictionary.

 ```python
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
```
Example dictionary

 ```python
discounted_total = calculate_discounted_total(basket, product_prices)
```
 Calculate and print the discounted total


 ```python
print(f"Discounted Total: ${discounted_total:.2f}")
```
Print

**📊 Out Put**
```
Discounted Total: $4.68

```

## Object-Oriented Programming (OOP): 
### Task 3: 
 **📑 Code Explanation**
```python
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
```
create class

 ```python
    def calculate_total(self):
        return self.price * self.quantity
```
method to calculate total price

 ```python
apple_product = Product(name='banana', price=4.0, quantity=7)
```
an instance of the Product class


 ```python
print(f"Product Name: {apple_product.name}")
print(f"Price per unit: ${apple_product.price}")
print(f"Quantity: {apple_product.quantity}")
print(f"Total Cost: ${apple_product.calculate_total():.2f}")

```
Access and print the attributes

**📊 Out Put**
```
Product Name: banana
Price per unit: $4.0
Quantity: 7
Total Cost: $28.00

```
### Task 4: 
 **📑 Code Explanation**
```python
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
```
create class

 ```python
    def calculate_total(self):
        return self.price * self.quantity
```
method to calculate total price

 ```python
  def calculate_total_cost_for_quantity(self, quantity):
        return self.price * quantity  
```
method to calculate total price for quantity

 ```python
apple_product = Product(name='banana', price=4.0, quantity=7)
```
an instance of the Product class


 ```python
print(f"Product Name: {apple_product.name}")
print(f"Price per unit: ${apple_product.price}")
print(f"Quantity: {apple_product.quantity}")
print(f"Total Cost for 7 units: ${apple_product.calculate_total():.2f}")

```
Access and print the attributes

 ```python
quantity_to_calculate = 4
total_cost_for_quantity = apple_product.calculate_total_cost_for_quantity(quantity_to_calculate)
print(f"Total Cost for {quantity_to_calculate} units: ${total_cost_for_quantity:.2f}")

```
Calculate the total cost for a specific quantity

**📊 Out Put**
```
Product Name: banana
Price per unit: $4.0
Quantity: 7
Total Cost for 7 units: $28.00
Total Cost for 4 units: $16.00

```
## Files I/O and Data Handling: 
### Task 5: 
 **📑 Code Explanation**
```python
import pandas as pd
```
import pandas laibrary 

 ```python
   def calculate_sales_statistics(data):
        total_revenue = (data['quantity'] * data['price']).sum()
        average_price_per_item = data['price'].mean()
        return total_revenue, average_price_per_item
```
This function takes a pandas DataFrame (data) as an argument,then calculate total revenue and average price per item from the given sales data

 ```python
  input_csv_path = 'sales_data.csv' 
  sales_data = pd.read_csv(input_csv_path) 
```
Read the CSV file

 ```python
total_revenue, average_price_per_item = calculate_sales_statistics(sales_data)
```
Calculate total revenue and average price per item


 ```python
print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Average Price per Item: ${average_price_per_item:.2f}")

```
print 

 ```python
output_csv_path = 'sales_results.csv'  
results_df = pd.DataFrame({'Total Revenue': [total_revenue], 'Average Price per Item': [average_price_per_item]})
results_df.to_csv(output_csv_path, index=False)

print(f"Results saved to '{output_csv_path}'.")

```
Save the results to a new CSV file
**📊 In Put File**
```
product_name,quantity,price
Apple,5,1.0
Banana,3,0.5
Orange,2,1.2
Grape,4,2.0
```
**📊 Out Put File**
```
Total Revenue,Average Price per Item
16.9,1.175

```
