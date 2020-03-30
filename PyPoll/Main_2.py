import os
import csv

# Tell Python where to collect data from
pypoll_csv = os.path.join('.', 'Resources', 'election_data.csv')


with open(pypoll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#Skip header row
    header = next(csvreader)
  
    voter = 0
#Formula to find the amount of voters
    for row in csvreader:
        voter += 1
    
with open(pypoll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#Skip Header row
    header = next(csvreader)
#Set values
    candidates_total = []
    candididates_list = []
    counts = []
    count = 0
    countss = 0
    countsss = 0
    countssss = 0
    winner = 0
#Append column so we can pull names from csv file
    for row in csvreader:
        candidates_total.append(row[2])

with open(pypoll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
#Finding the amount of times a candidate received a vote 
    for row in csvreader:
        candidate = (row[2])
        count = count + (candidate.count("Khan"))
        countss = countss + (candidate.count("Correy"))
        countsss = countsss + (candidate.count("Li"))
        countssss = countssss + (candidate.count("O'Tooley"))
#Formula for finding percent value
    Percent_Khan = (round((count/voter)*100))
    Percent_Correy = (round((countss/voter)*100))
    Percent_Li = (round((countsss/voter)*100))
    Percent_O = (round((countssss/voter)*100))


#Create Lists to be zipped
candididates_list = ["Khan", "Correy", "Li", "O'Tooley"]
counts = [count, countss, countsss, countssss]

#Create zip of the two appended lists to pull values from both
voter_count = zip(candididates_list, counts)
#Set value for increase and decrease
winner = max(counts)

with open(pypoll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')   
#Use if function to pull the matching value from column[0] and column[1] and print the date from column[0]
    for line in voter_count:
        if line [1] == winner:
            winner_name = line[0]
#Print Text
    print("Election Results")
    print(f"Total Votes: {voter}")
    print(f"Khan %{str(Percent_Khan)} ({(count)})")
    print(f"Correy %{str(Percent_Correy)} ({(countss)})")
    print(f"Li %{str(Percent_Li)} ({(countsss)})")
    print(f"O'Tooley %{str(Percent_O)} ({(countssss)})")
    print(f"Winner: {str(winner_name)}")

#Create text file to write into   
    file = open('python.txt', 'w')
#Write print values into text file
    file.write("Election Results")
    file.write(f"Total Votes: {voter}")
    file.write(f"Khan %{str(Percent_Khan)} ({(count)})")
    file.write(f"Correy %{str(Percent_Correy)} ({(countss)})")
    file.write(f"Li %{str(Percent_Li)} ({(countsss)})")
    file.write(f"O'Tooley %{str(Percent_O)} ({(countssss)})")
    file.write(f"Winner: {str(winner_name)}")
    file.close()