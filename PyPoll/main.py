#Reed Zimpfer
#Module 3 Challenge
#PyPoll

import os
import csv

# Set path for accessing data and writing to output file
csvpath = os.path.join("Resources", "election_data.csv")
output = os.path.join("analysis", "output.txt")

# Open the CSV

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    #Declaring variables
    votes = []
    county = []
    candidates = []
    Charles = []
    Diana = []
    Raymon = []

    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    # The total number of votes cast.
    total_votes = (len(votes))

    # A complete list of candidates who received votes.
    for candidate in candidates:
        if candidate == "Charles Casper Stockham":
            Charles.append(candidates)    
        elif candidate == "Diana DeGette":
            Diana.append(candidates)
        elif candidate == "Raymon Anthony Doane":
            Raymon.append(candidates)
    
    # The total Number of votes each candidate won.
    charles_votes = len(Charles)
    diana_votes = len(Diana)
    raymon_votes = len(Raymon)
    #print(charles_votes)
    #print(diana_votes)
    #print(raymon_votes)
    
    # The Percentage of votes each candidate won.
    charles_percent = round(((charles_votes / total_votes) * 100), 3)
    diana_percent = round(((diana_votes / total_votes) * 100), 3)
    raymon_percent = round(((raymon_votes / total_votes) * 100), 3)
    
    #print(charles_percent)
    #print(diana_percent)
    #print(raymon_percent)
    
    # Choosing the winner of the election based on popular vote.
    if charles_percent > max(diana_percent, raymon_percent):
        winner = "Charles Casper Stockham"
    elif diana_percent > max(charles_percent, raymon_percent):
        winner = "Diana Degette"  
    else:
        winner = "Raymon Anthony Doane"

    #Print Statements to the terminal
    print(f"\n" + "Election Results" )
    print(f"----------------------------------------------------" + "\n")
    print(f"Total Votes: {total_votes}" + "\n")
    print(f"----------------------------------------------------" + "\n")
    print(f"Charles Casper Stockham: {charles_percent}% ({charles_votes})" + "\n")
    print(f"Diana DeGette: {diana_percent}% ({diana_votes})" + "\n")
    print(f"Raymon Anthony Doane: {raymon_percent}% ({raymon_votes})" + "\n")
    print(f"----------------------------------------------------" + "\n")
    print(f"Winner: {winner}" + "\n")
    print(f"----------------------------------------------------")

# Write statements to the output file
with open(output,"w") as txt_file:
    txt_file.write(
        f"\nElection Results\n"
        f"-------------------------------------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------------------------------------------\n"
        f"Charles Casper Stockham: {charles_percent}% ({charles_votes})\n"
        f"Diana DeGette: {diana_percent}% ({diana_votes})\n"
        f"Raymon Anthony Doane: {raymon_percent}% ({raymon_votes})\n"
        f"---------------------------------------------------\n"
        f"Winner: {winner}\n"
        f"---------------------------------------------------\n"
    )