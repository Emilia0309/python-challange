#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# load data set
file_url = (r'C:\Users\amyee\OneDrive\Desktop\Pro\python-challange\PyBank\Resources\budget_data.csv')

try:
    # Load the dataset
    df = pd.read_csv(file_url)
    
    # Print column names and first few rows for inspection
    print("Columns:", df.columns)
    print("First few rows:\n", df.head())

    # Rename columns if necessary (e.g., stripping whitespace)
    df.columns = df.columns.str.strip()
    
    # Check if 'Date' column exists
    if 'Date' not in df.columns:
        raise ValueError("The 'Date' column is missing from the data.")

    # Inspect the unique values to determine date format
    print("Unique date values:\n", df['Date'].unique())

    # Explicitly specify the date format if known, e.g., '%b-%y' for 'Jan-10'
    # Replace '%b-%y' with the actual format if different
    df['Date'] = pd.to_datetime(df['Date'], format='%b-%y', errors='coerce')

    # Check for any NaT values
    if df['Date'].isna().any():
        print("Some dates could not be parsed:")
        print(df[df['Date'].isna()])

    # Sort data by date
    df = df.sort_values(by='Date')
    
    # Calculate the total number of months
    total_months = df.shape[0]
    
    # Calculate the net total amount of "Profit/Losses"
    net_total = df['Profit/Losses'].sum()
    
    # Calculate the changes in "Profit/Losses"
    df['Change'] = df['Profit/Losses'].diff()
    
    # Calculate the average change in "Profit/Losses"
    average_change = df['Change'].mean()
    
    # Find the greatest increase in profits
    greatest_increase = df.loc[df['Change'].idxmax()]
    
    # Find the greatest decrease in profits
    greatest_decrease = df.loc[df['Change'].idxmin()]
    
    # Prepare results for printing and saving
    results = (
        f"Total number of months: {total_months}\n"
        f"Net total amount of 'Profit/Losses': ${net_total:,.2f}\n"
        f"Average change in 'Profit/Losses': ${average_change:,.2f}\n"
        f"Greatest increase in profits: {greatest_increase['Date'].strftime('%b-%Y')} (${greatest_increase['Change']:,.2f})\n"
        f"Greatest decrease in profits: {greatest_decrease['Date'].strftime('%b-%Y')} (${greatest_decrease['Change']:,.2f})"
    )

    # Print results to the terminal
    print(results)

    # Export results to a text file
  
    with open(r'C:\Users\amyee\OneDrive\Desktop\Pro\python-challange\PyBank\analysis\financial_analysis.txt', 'w') as file:
        file.write(results)



except pd.errors.EmptyDataError:
    print("No columns to parse from file. The CSV file might be empty or incorrectly formatted.")
except pd.errors.ParserError:
    print("Error parsing the CSV file. Please check the file format.")
except ValueError as ve:
    print(f"ValueError: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# In[ ]:




