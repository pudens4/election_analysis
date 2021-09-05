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

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    # for row in file_reader:
    #     #print(row)
    