#Start by importing
import os
import csv

#Set path
csvfile = os.path.join("Resources", "election_data.csv")


#Set variables
count = 0
candidatelist = []
the_candidate = []
vote_count = []
vote_percent = []

#Open the CSV using the set path csvfile

with open(csvfile) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # Conduct the ask
    for row in csvreader:
        #Count the total number of votes
        count = count + 1
        #Set the candidate names to candidatelist
        candidatelist.append(row[2])
        #Create a set from the candidatelist to get the candidates names
    for x in set(candidatelist):
        the_candidate.append(x)
        #y is the total number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        #z is the percent of total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = the_candidate[vote_count.index(winning_vote_count)]
    
#Print to terminal

print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for _ in range(len(the_candidate)):
            print(the_candidate[_] + ": " + str(vote_percent[_]) +"% (" + str(vote_count[_])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

#Print to a text file: election_results.txt

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for _ in range(len(set(the_candidate))):
        text.write(the_candidate[_] + ": " + str(vote_percent[_]) +"% (" + str(vote_count[_]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")
