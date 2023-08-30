# UofT SCS EdX Data Bootcamp
# Challenge 3. Part 1: PyBank
# Script Author: Tania Barrera (tsbarr)
# -----------------------------------------

# import modules
import os
import csv

# --- for storing output
totalMonths = 0  # count months
totalChange = 0  # sum all changes
minChange = ["", 0]  # lowest change and its date [date, change]
maxChange = ["", 0]  # highest change and its date [date, change]

# --- input source path
csvpath = os.path.join('resources', 'budget_data.csv')

# ------- open file stream --------
# open input csv file using path
with open(csvpath) as csvfile:
    # csv reader, columns: date, change
    csvreader = csv.reader(csvfile, delimiter=',')

    # get headers
    headers = next(csvreader)

    # iterate through rest of rows
    for row in csvreader:
        # get data from this row
        thisDate = row[0]
        thisChange = int(row[1])  # cast str to int

        # increase totalMonths by 1
        totalMonths += 1

        # increase totalchange by thisChange
        totalChange += thisChange

        # check if thisChange is lower than minChange
        if thisChange < minChange[1]:
            # if so, update minChange with current row
            minChange = [thisDate, thisChange]

        # check if thisChange is higher than minChange
        if thisChange > maxChange[1]:
            # if so, update maxChange with current row
            maxChange = [thisDate, thisChange]
# ------- close file stream --------

# average change is totalChange / totalMonths
averageChange = totalChange / totalMonths

# we now have all necessary values, so we format the output in a string
outputS = f"Financial Analysis\n\n------------------------\n\nTotal Months: {totalMonths}\n\nTotal: {totalChange}\n\nAverange Change: {averageChange}\n\nGreatest Increase in Profits: {maxChange[0]} ({maxChange[1]})\n\nGreatest Decrease in Profits: {minChange[0]} ({minChange[1]})"

# write output to file


# print output to console
print(outputS)
