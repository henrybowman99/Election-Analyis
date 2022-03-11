
#Add dependencies to access/load data
import csv
import os

# create variable that holds election results csv
file_to_load = os.path.join("Resources", "election_results.csv")
# create variable thats holds/creates path to election analysis results text file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize variable to hold track total votes cast
total_votes = 0

#create list that will hold each candidate
candidate_list = []
#create dictionary that holds candidates as keys and their vote count as value
candidate_votes = {}

#create list that will hold each county
counties = []
#create dictionary that holds counties as keys and their vote count as value
county_votes = {}



# track winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#  track largest county and its turnout
top_county = ""
top_county_turnout = 0




# read in CSV file as dictionary
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # read header
    header = next(reader)

    # loop through rows in csv file
    for row in reader:

        # for each row add a tally to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate = row[2]

        # extract the county name from each row and save it in a var
        county = row[1]


        # if candidate is not already in the candidate list
        if candidate not in candidate_list:

            # add candidate to the candidate list.
            candidate_list.append(candidate)

            # begin tracking that candidate's voter count.
            candidate_votes[candidate] = 0

        # add a vote to candidates vote count
        candidate_votes[candidate] += 1

        #check if county is in counties or not
        if county not in counties:
            
            # if it's a new county add to counties list
            counties.append(county)


            # start counting county turnout
            county_votes[county] = 0


        # add vote to that county's vote count.
        county_votes[county] += 1



# save the results to text file.
with open(file_to_save, "w") as txt_file:

    # print the final vote count to terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    #write total votes into txt file
    txt_file.write(election_results)

    # loop through counties in county_votes dictionary
    for county in county_votes:
        

        #save votes for each county in a variable
        votes_for_county = county_votes.get(county)

        # get percentage of votes for each county by dividing county votes by total votes
        county_vote_percentage = float(votes_for_county)/float(total_votes)*100

         # create string that reports total votes and vote percentage for each county
        county_results = (f"{county}: {county_vote_percentage: .1f}% ({votes_for_county:,})\n")
        
        #print county resuts to terminal
        print(county_results)
        #add county results to the same text file
        txt_file.write(county_results)

         # determine if county is currently leading and if it is change it to the top county and its turnout to the top turnout
        if (votes_for_county > top_county_turnout):
            top_county_turnout = votes_for_county
            top_county = county


    #save county results in new variable
    county_turnout_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {top_county}\n"
        f"Number of Votes: {top_county_turnout}\n"
        f"-------------------------\n")
    # print county results to terminal
    print(county_turnout_summary)

    


    # add county results to text file
    txt_file.write(county_turnout_summary)


    # loop through candidate_votes dictionary
    for candidate_name in candidate_votes:

        # calculate vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        # create string for candidate vote count
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print candidate results to terminal
        print(candidate_results)
        #  save candidate results to text file.
        txt_file.write(candidate_results)

        #determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # print the winning candidate to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    
    print(winning_candidate_summary)

    # add winning candidate summary to text file
    txt_file.write(winning_candidate_summary)
