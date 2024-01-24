import os
import csv

#path for csv file
csvpath = os.path.join("Resources", "election_data.csv")

#creating list/dic to use
data = []
votes = {}

#opening CSV and skipping header row with next
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    #adding data to list and creating variables
    for row in csvreader:
        BallotID = row[0]
        County = row[1]
        Candidate = row[2]
        data.append((BallotID, County, Candidate))
        #If candidate name has come up before, then add 1 to the total votes
        if Candidate in votes:
            votes[Candidate] += 1
        #Else candidate will be added and votes will be set at 1 for the first vote
        else:
            votes[Candidate] = 1
        #Process above allows autopopulation of candidates as opposed to manually putting them in

#These are to print into the terminal
print(f"Total Votes: {len(data)}")
print("Candidate Votes:")
for Candidate, vote_count in votes.items():
    percent = (vote_count/(len(data))) * 100
    print(Candidate, ":", vote_count, "(", round(percent, 3),"%)")
    winner = max(votes, key=votes.get)
print(winner)

#pathing to new file location for text, election results. in write mode 
output_path = os.path.join("Analysis","ElectionResults.txt")
with open(output_path, "w") as text:
    text.write("ElectionResults")
    text.write("\n""__________________________________________________________""\n")
    text.write(f"Total Votes: {len(data)}")
    text.write("\n""__________________________________________________________""\n")
#for statement is to display the candidates, without it only displays one candidate as opposed to all of them.
    for Candidate, vote_count in votes.items():
        text.write(f"{Candidate}: {vote_count} {round(percent, 3)}%")
        text.write("\n")
    text.write("__________________________________________________________""\n")
    text.write(f"Winner: {winner}")
