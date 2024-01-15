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
