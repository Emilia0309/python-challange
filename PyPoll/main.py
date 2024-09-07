#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

# Load the dataset
file_url = (r'C:\Users\amyee\OneDrive\Desktop\Pro\python-challange\PyPoll\Resources\election_data.csv')  # Replace with the actual URL or path to your CSV file

try:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_url)
    
    # Check if DataFrame is empty
    if df.empty:
        print("The DataFrame is empty. Please check the CSV file.")
    else:
        # Calculate the total number of votes cast
        total_votes = df.shape[0]
        
        # Get the list of candidates who received votes
        candidates = df['Candidate'].unique()
        
        # Calculate the total number of votes each candidate won
        votes_per_candidate = df['Candidate'].value_counts()
        
        # Calculate the percentage of votes each candidate won
        percentage_per_candidate = (votes_per_candidate / total_votes) * 100
        
        # Determine the winner of the election based on popular vote
        winner = votes_per_candidate.idxmax()
        
        # Prepare results for printing
        results = (
            f"Total number of votes cast: {total_votes}\n"
            f"Complete list of candidates: {', '.join(candidates)}\n\n"
        )
        
        results += "Vote Counts and Percentages:\n"
        for candidate in candidates:
            vote_count = votes_per_candidate[candidate]
            vote_percentage = percentage_per_candidate[candidate]
            results += (f"{candidate}: {vote_count} votes ({vote_percentage:.2f}%)\n")
        
        results += f"\nThe winner of the election is: {winner}\n"
        
          # Print results to the terminal
    print(results)

    # Export results to a text file
  
    with open(r'C:\Users\amyee\OneDrive\Desktop\Pro\python-challange\PyPoll\analysis\election_results.txt', 'w') as file:
        file.write(results)

except pd.errors.EmptyDataError:
    print("No columns to parse from file. The CSV file might be empty or incorrectly formatted.")
except pd.errors.ParserError:
    print("Error parsing the CSV file. Please check the file format.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

