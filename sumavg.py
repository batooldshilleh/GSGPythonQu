"""
Given a list of sales amounts for a week, calculate the total sales and average
sales. Print the results. 
"""
def calculate_sales_statistics(sales):
    total_sales = sum(sales)
    average_sales = total_sales / len(sales)
    return total_sales, average_sales


sales_week = [100, 150, 200, 120, 180, 250, 170]


total_sales, average_sales = calculate_sales_statistics(sales_week)


print("Total Sales: $", total_sales)
print("Average Sales: $", average_sales)
