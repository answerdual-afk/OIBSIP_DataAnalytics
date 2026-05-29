import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("retail_sales_dataset.csv")

# First 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Customer Analysis
print("\nAverage Age of Customers:")
print(df["Age"].mean())

print("\nGender Distribution:")
print(df["Gender"].value_counts())

# Product Category Analysis
print("\nProduct Category Sales:")
print(df["Product Category"].value_counts())

print("\nTotal Sales by Product Category:")
print(df.groupby("Product Category")["Total Amount"].sum())

# Convert Date column to proper format
df["Date"] = pd.to_datetime(df["Date"])

# Monthly Sales Trend
monthly_sales = df.groupby(df["Date"].dt.month)["Total Amount"].sum()

print("\nMonthly Sales Trend:")
print(monthly_sales)

# Gender Distribution Chart
df["Gender"].value_counts().plot(kind="bar")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# Product Category Sales Chart
df.groupby("Product Category")["Total Amount"].sum().plot(kind="bar")
plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.show()

# Monthly Sales Trend
monthly_sales.plot(kind="line")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()