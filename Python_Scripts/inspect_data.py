import pandas as pd


file_path = 'zomato.csv'

try:
    # Load the dataset into a pandas DataFrame
    df = pd.read_csv(file_path, encoding='latin1') 

    # --- Get the information we need ---

    # 1. Print all the column names
    print("--- Column Names ---")
    print(df.columns.tolist())
    print("\n" + "="*30 + "\n") # Separator

    # 2. Print the first 5 rows of the data to see what it looks like
    print("--- First 5 Rows of Data ---")
    print(df.head())

except FileNotFoundError:
    print(f"Error: The file was not found at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")