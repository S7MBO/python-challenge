# File main.py

# Import modules
import os
import csv

# Set parameters of the variables
total_votes = 0
candidate_names = []
candidate_votes = {}
winner = ""
winning_count = 0

# Load the source file
source_file = os.path.join("Resources", "election_data.csv")

# Specify the exported file location
winning_candidate_summary = os.path.join("Analysis", "Election_Analysis.txt")

# Open and Read CSV source file
with open(source_file) as election_data:
    csvreader = csv.reader(election_data)

    # Read header row first
    csvheader = next(csvreader)

    # For each row...
    for row in csvreader:

        # Run the loader animation
        print(". ", end=""),

        # Add to the total vote count
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        # (In a way, our loop is "discovering" candidates as it goes)
        if candidate_name not in candidate_names:

            # Add it to the list of candidates in the running
            candidate_names.append(candidate_name)

            # And begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        # Then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print the results and export the data to our text file
with open(winning_candidate_summary, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"\n"
        f"Total Votes: {total_votes}\n"
        f"\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winner = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"\n"
        f"Winner: {winner}\n"
        f"\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)