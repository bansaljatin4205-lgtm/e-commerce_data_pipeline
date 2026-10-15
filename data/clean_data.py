import pandas as pd

# Load the orders data
df = pd.read_csv("data/orders.csv")

# Remove duplicate orders
df = df.drop_duplicates(subset="order_id")

# Remove rows with missing values
df = df.dropna()

# Convert order_date into date format
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

# Remove rows with invalid dates
df = df.dropna(subset=["order_date"])

# Calculate revenue
df["revenue"] = df["quantity"] * df["price"]

# Save cleaned data
df.to_csv("data/cleaned_orders.csv", index=False)

print("Data cleaning completed successfully!")
print("Total orders:", len(df))
print("Total revenue: ₹", df["revenue"].sum())
print("Cleaned file saved as data/cleaned_orders.csv")