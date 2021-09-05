'''
data retrieve
Total number of votes cast
A complete list of candidates who received votes
Total number of votes each candidate received
Percentage of votes each candidate won
The winner of the election based on popular vote


path to csv
Resources/election_results.csv
'''

import csv
dir(csv)

#direct path

#file_to_load = 'Resources/election_results.csv'
# election_data = open(file_to_load, 'r')

# election_data.close

#with open(file_to_load) as election_data:

#    print(election_data)

'..'
#indirect path to file


import os

# file_to_load = os.path.join("Resources", "election_results.csv")

# with open (file_to_load) as election_data:
#       print(election_data)


# # # Create a filename variable to a direct or indirect path to the file.

# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # # Using the open() function with the "w" mode we will write data to the file.
# # open(file_to_save, "w")


# # outfile = open( file_to_save, "w")

# # outfile.write("Hello World")

# # outfile.close()

# with open (file_to_save, "w") as txt_file:
#      txt_file.write("Counties in the Election\n-----------------------------\nArapahoe\nDenver\nJefferson")



# file_reader = csv.reader(election_data)



# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# total vote counter
total_votes = 0 


candidate_options = []
#empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    for row in file_reader:
        total_votes +=1
        #print(row)

        candidate_name = row[2]

        if candidate_name not in candidate_options:
        
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0 

        #add a vote to candidate counts
        candidate_votes[candidate_name] += 1



    
#print(total_votes)

#print(candidate_options)

print(candidate_votes)


for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage}% of the vote.")


    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

