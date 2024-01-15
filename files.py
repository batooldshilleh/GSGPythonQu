import pandas as pd

def calculate_sales_statistics(data):
    total_revenue = (data['quantity'] * data['price']).sum()
    average_price_per_item = data['price'].mean()
    return total_revenue, average_price_per_item

# Read the CSV file
input_csv_path = 'sales_data.csv'  # Replace with your actual file path
sales_data = pd.read_csv(input_csv_path)

# Calculate total revenue and average price per item
total_revenue, average_price_per_item = calculate_sales_statistics(sales_data)

# Display the results
print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Average Price per Item: ${average_price_per_item:.2f}")

# Save the results to a new CSV file
output_csv_path = 'sales_results.csv'  # Replace with your desired output file path
results_df = pd.DataFrame({'Total Revenue': [total_revenue], 'Average Price per Item': [average_price_per_item]})
results_df.to_csv(output_csv_path, index=False)

print(f"Results saved to '{output_csv_path}'.")

