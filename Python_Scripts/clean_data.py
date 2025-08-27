import pandas as pd
import numpy as np

# File paths for input and output
input_file = 'zomato.csv'
output_file = 'zomato_cleaned.csv'

print("Starting data cleaning process...")

try:
    # Load the dataset
    df = pd.read_csv(input_file, encoding='latin1')
    print(f"Successfully loaded {input_file}. Shape: {df.shape}")

    # --- Step 1: Drop unnecessary columns ---
    # These columns are not useful for our dashboard analysis.
    columns_to_drop = ['url', 'address', 'phone', 'dish_liked', 'reviews_list', 'menu_item']
    df.drop(columns=columns_to_drop, inplace=True)
    print(f"Dropped unnecessary columns. New shape: {df.shape}")

    # --- Step 2: Clean the 'rate' column ---
    # The 'rate' is a string like "4.1/5". We need to make it a number.
    df['rate'] = df['rate'].str.replace('/5', '').str.strip()
    df['rate'] = df['rate'].replace('NEW', np.nan) # Replace 'NEW' with a null value
    df['rate'] = df['rate'].replace('-', np.nan)   # Replace '-' with a null value
    df['rate'] = pd.to_numeric(df['rate']) # Convert the column to a number (float)
    print("Cleaned 'rate' column.")

    # --- Step 3: Clean and rename 'approx_cost(for two people)' ---
    # This column is a string with commas. We need to make it a number.
    df.rename(columns={'approx_cost(for two people)': 'cost_for_two'}, inplace=True)
    df['cost_for_two'] = df['cost_for_two'].str.replace(',', '').astype(float)
    print("Cleaned and renamed 'cost_for_two' column.")

    # --- Step 4: Handle missing values ---
    # We will remove rows where crucial information like 'rate' or 'rest_type' is missing.
    df.dropna(subset=['rate', 'rest_type', 'cost_for_two', 'cuisines'], inplace=True)
    print(f"Dropped rows with missing values. New shape: {df.shape}")

    # --- Step 5: Save the cleaned data to a new file ---
    df.to_csv(output_file, index=False)
    print(f"\nData cleaning complete! Cleaned data saved to '{output_file}'")

except FileNotFoundError:
    print(f"Error: The file was not found at {input_file}")
except Exception as e:
    print(f"An error occurred: {e}")