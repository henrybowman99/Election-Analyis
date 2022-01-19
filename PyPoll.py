# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
        # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
  
    #print each row
    for row in file_reader:
        total_votes += 1
        #print candidate name from each row
        candidate_name = row[2]
        #add name to list if not already added
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        #add up candidtate votes
        candidate_votes[candidate_name] += 1
    
    print(total_votes)
    print(candidate_options)
    print(candidate_votes)


# Determine the percentage of votes for each candidate by looping through the counts.
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    #Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")



    
    #find winning candidtate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
    
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)



