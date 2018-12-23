# File: main.py
import os
import csv

# variable to store file path

election_data = os.path.join("Resources","election_data.csv")

# List to store candidate names
candidate = []

# List to store number of votes each candidate received
num_vote = []

# List to store % of votes each candidate received
percent_vote = []

# A counter for total number of votes
total_votes = 0

#open the file in read mode
with open(election_data, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Reading the header row
    header_row = next(csv_reader)

    for rows in csv_reader:

        # set the counter to 1
        total_votes += 1

        # If condition for adding candidates in the list
        if rows[2] not in candidate:
            candidate.append(rows[2])
            index = candidate.index(rows[2])
            num_vote.append(1)
        else:
            index = candidate.index(rows[2])
            num_vote[index] += 1
    
    # add to percent_vote list
    for votes in num_vote:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percent_vote.append(percentage)

# Find the winning candidate
winner = max(num_vote)
index = num_vote.index(winner)
winning_candidate = candidate[index]

# Displaying results
print("Election Results\n")
print("--------------------------\n")
print(f"Total Votes: {str(total_votes)}\n")
print("--------------------------\n")
for i in range(len(candidate)):
    print(f"{candidate[i]}: {str(percent_vote[i])}% ({str(num_vote[i])})\n")
print("--------------------------\n")
print(f"Winner: {winning_candidate}\n")
print("-------------------------\n")

# write to output file
output = open("output.txt", "w")

output.write("Election Results\n")
output.write("--------------------------\n")
output.write(f"Total Votes: {str(total_votes)}\n")
output.write("--------------------------\n")

for i in range(len(candidate)):
    output.write(f"{candidate[i]}: {str(percent_vote[i])} ({str(num_vote[i])})\n")
    
output.write("--------------------------\n")
output.write(f"Winner: {winning_candidate}\n")
output.write("--------------------------\n")