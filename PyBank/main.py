import csv
from pathlib import Path
from datetime import datetime
import os


data_file = Path('OneDrive')/'Desktop'/'Pro' / 'python-challange' / 'PyBank'/ 'Resources' / 'budget_data.csv'



# Print paths for debugging
print(f"Data file path: {data_file.resolve()}")

try:
    # Read the CSV file
    with open(data_file, newline='') as csvfile:
        reader = csv.reader(csvfile)




        # Skip the header row
        header = next(reader)
        
        if 'Date' not in header or 'Profit/Losses' not in header:
            raise ValueError("The required 'Date' or 'Profit/Losses' column is missing from the data.")

        data = []
        for row in reader:
            date_str = row[0].strip()
            profit_losses_str = row[1].strip()

            try:
                # Parse the date
                date = datetime.strptime(date_str, '%b-%y')

                # Convert profit/losses to integer
                profit_losses = int(profit_losses_str)
            except ValueError as ve:
                print(f"Error parsing row: {row}. Error: {ve}")
                continue

            data.append((date, profit_losses))

        if len(data) == 0:
            raise ValueError("No valid data found in the CSV file.")

        # Sort data by date
        data.sort(key=lambda x: x[0])

        # Calculate the total number of months
        total_months = len(data)

        # Calculate the net total amount of "Profit/Losses"
        net_total = sum([row[1] for row in data])

        # Calculate the changes in "Profit/Losses"
        changes = [data[i][1] - data[i-1][1] for i in range(1, total_months)]

        # Calculate the average change in "Profit/Losses"
        average_change = sum(changes) / len(changes) if len(changes) > 0 else 0

        # Find the greatest increase in profits
        greatest_increase_index = changes.index(max(changes)) + 1
        greatest_increase = data[greatest_increase_index]

        # Find the greatest decrease in profits
        greatest_decrease_index = changes.index(min(changes)) + 1
        greatest_decrease = data[greatest_decrease_index]

        # Prepare results for printing and saving
        results = (
            f"Total number of months: {total_months}\n"
            f"Net total amount of 'Profit/Losses': ${net_total:,.2f}\n"
            f"Average change in 'Profit/Losses': ${average_change:,.2f}\n"
            f"Greatest increase in profits: {greatest_increase[0].strftime('%b-%Y')} (${max(changes):,.2f})\n"
            f"Greatest decrease in profits: {greatest_decrease[0].strftime('%b-%Y')} (${min(changes):,.2f})"
        )

        # Print results to the terminal
        print(results)
        
         # Define path for output file
        output_file = Path('OneDrive')/'Desktop'/'Pro' / 'python-challange' / 'PyBank'/ 'analysis' / 'financial_analysis.txt'
       
        
        # Export results to a text file
        with open(output_file, 'w') as file:
            file.write(results)



except FileNotFoundError:
    print("The file was not found. Please check the file path.")
except ValueError as ve:
    print(f"ValueError: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")