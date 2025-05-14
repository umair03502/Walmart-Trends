import pandas as pd

# Load the dataset
df = pd.read_csv("Walmart.csv")

# 1. Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

# 2. Remove duplicate rows
df_cleaned = df.drop_duplicates()

# 3. Remove invalid Weekly_Sales (e.g., negative values)
df_cleaned = df_cleaned[df_cleaned['Weekly_Sales'] >= 0]

# 4. (Optional) Ensure Holiday_Flag contains only 0 or 1
df_cleaned = df_cleaned[df_cleaned['Holiday_Flag'].isin([0, 1])]

# Preview the cleaned data
print(df_cleaned.head())

# (Optional) Save cleaned dataset to a new CSV
df_cleaned.to_csv("Walmart_Cleaned.csv", index=False)
