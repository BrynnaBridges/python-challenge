import os
import csv

# Tell Python where to collect data from
pybank_csv = os.path.join('.', 'Resources', 'budget_data.csv')

with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#Skip Header
    header = next(csvreader)
#Set total months to 0
    total_months = 0
#open loop with function to find total months
    for line in csvreader:
        total_months = total_months + 1

with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#Skip header
    header = next(csvreader)
#Set Variables
    total_money = []
    dates_list = []
    average_change = []
    total_change = 0
#Append column in order to loop through values
    for row in csvreader:
        total_money.append((int(row[1])))
        dates_list.append(row[0])
#Find Sum of the money
    for line in total_money:
        total = sum(total_money)

with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#Skip header
    header = next(csvreader)
#Loop through append to pull values in order to find change in money values    
    for row in range(len(total_money)-1):
        average_change.append(int(total_money[row+1]) - int(total_money [row]))
        total_change = ((sum(average_change)) / 85)

with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#Create zip of the two appended lists to pull values from both
    Greatest = zip(dates_list, average_change)
#Set value for increase and decrease
    increase = max(average_change)
    decrease = min(average_change)
 #Use if function to pull the matching value from column[0] and column[1] and print the date from column[0]
    for line in Greatest:
        if line [1] == increase:
            increase_date = line[0]
        elif line [1] == decrease:
            decrease_date = line[0]
#Print Text
    print("Financial Analysis")
    print(f"Total Months: {total_months}")
    print(f"Total: {total}")
    print(f"Average Change: {total_change}")
    print(f"Greatest Increase in Profits: {increase_date} ({increase})")
    print(f"Decrease in Profits: {decrease_date} ({decrease})")

#Create text file to write into
    file = open('python.txt', 'w')
#Write print values into text file
    file.write("Financial Analysis")
    file.write(f"Total Months: {total_months}")
    file.write(f"Total: {total}")
    file.write(f"Average Change: {total_change}")
    file.write(f"Greatest Increase in Profits: {increase_date} ({increase})")
    file.write(f"Decrease in Profits: {decrease_date} ({decrease})")
    file.close()
