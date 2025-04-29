import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv(r"C:\Users\astik\Downloads\superMarketDataset.csv")

# Preview data
print(df.head())

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

#  Total Sales (Total = Unit Price × Quantity)
df['Total_Sales'] = df['Unit price'] * df['Quantity']

#  Average Basket Size
avg_basket = df['Quantity'].mean()
print(f"Average Basket Size: {avg_basket:.2f}").

#  (Line Graph) Daily Sales Over Time
daily_sales = df.groupby('Date')['Total_Sales'].sum()
plt.figure(figsize=(10, 5))
daily_sales.plot()
plt.title('Daily Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

# ( Bar Graph ) Total Sales by Product Line
sales_by_product = df.groupby('Product line')['Total_Sales'].sum().sort_values()
sales_by_product.plot(kind='barh', figsize=(8, 5), color='skyblue')
plt.title('Total Sales by Product Line')
plt.xlabel('Total Sales')
plt.ylabel('Product Line')
plt.tight_layout()
plt.show()

# Sales by City
sales_by_city = df.groupby('City')['Total_Sales'].sum()
sales_by_city.plot(kind='pie', autopct='%1.1f%%', figsize=(6, 6), startangle=140)
plt.title('Sales Distribution by City')
plt.ylabel('')
plt.tight_layout()
plt.show()

# Label Encoding for Categorical Features
encoder = LabelEncoder()
df['Gender_Encoded'] = encoder.fit_transform(df['Gender'])
df['Customer_Type_Encoded'] = encoder.fit_transform(df['Customer type'])
print(df[['Gender', 'Gender_Encoded', 'Customer type', 'Customer_Type_Encoded']].head())
