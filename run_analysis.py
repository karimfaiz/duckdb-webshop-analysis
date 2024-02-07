import duckdb
import pandas as pd
import matplotlib.pyplot as plt

# Create a DuckDB connection
con = duckdb.connect(database=':memory:')  # In-memory database

# Read data from the Parquet file into a Pandas DataFrame
df = pd.read_parquet('my_shop_data.parquet')

# Register the Pandas DataFrame as a DuckDB table
con.register('my_shop', df)

# Execute SQL queries to retrieve data
query = "SELECT category, COUNT(*) as total_orders, AVG(price) as avg_price FROM my_shop GROUP BY category"
result = con.execute(query)

# Fetch the result into a DataFrame
result_df = pd.DataFrame(result.fetchall(), columns=["Category", "Total Orders", "Average Price"])

# Display the result
print(result_df)




# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(result_df["Category"], result_df["Total Orders"])
plt.xlabel("Category")
plt.ylabel("Total Orders")
plt.title("Total Orders by Category")
plt.xticks(rotation=45)
plt.show()

