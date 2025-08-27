import pandas as pd

# The file path to your CLEANED Zomato CSV file.
file_path = 'zomato_cleaned.csv'

print(f"--- Verifying data from: {file_path} ---\n")

try:
    # Load the cleaned dataset
    df = pd.read_csv(file_path)

    # --- Verification Step 1: Look at the first 10 rows ---
    print("--- First 10 Rows of Cleaned Data ---")
    print(df.head(10))
    print("\n" + "="*50 + "\n")

    # --- Verification Step 2: Check the data types and look for missing values ---
    # This is the most important check.
    # Look for the following:
    #   - 'rate' and 'cost_for_two' should be 'float64' (a number).
    #   - The 'Non-Null Count' for all columns should be the same, which means no missing values.
    print("--- Data Summary (Data Types and Non-Null Counts) ---")
    df.info()

except FileNotFoundError:
    print(f"Error: The file was not found at {file_path}. Make sure you ran the clean_data.py script first.")
except Exception as e:
    print(f"An error occurred: {e}")