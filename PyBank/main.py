# UofT SCS EdX Data Bootcamp
# Challenge 3. Part 1: PyBank
# Script Author: Tania Barrera (tsbarr)
# -----------------------------------------

# import modules
import os
import csv

# --- for storing output
totalMonths = 0  # count months
totalPL = 0  # sum all profit/losses
totalChange = 0  # calculate difference from prev PL for each and sum all, to calculate average later
# max decrease = min Change in PL and its date [date, decrease]
minChange = ["", 0]
# max increase = max Change in PL and its date [date, increase]
maxChange = ["", 0]

# --- input source path
csvpath = os.path.join('resources', 'budget_data.csv')

# ------- open file stream --------
# open input csv file using path
with open(csvpath) as csvfile:
    # csv reader, columns: date, change
    csvreader = csv.reader(csvfile, delimiter=',')

    # get headers
    headers = next(csvreader)

    # get first row before itaring
    # because we are not calculating change for it
    # but we need it to calculate the first change
    firstRow = next(csvreader)
    # count first month and profit/losses
    totalMonths = 1
    totalPL = int(firstRow[1])  # cast str to int
    # set previousPL to profit/losses of first month
    previousPL = int(firstRow[1])  # cast str to int

    # iterate through rest of rows
    for row in csvreader:
        # get data from this row
        thisDate = row[0]
        thisPL = int(row[1])  # cast str to int

        # increase totalMonths by 1
        totalMonths += 1
        # increase totalPL by thisPL
        totalPL += thisPL

        # calculate thisChange
        thisChange = thisPL - previousPL
        # increase totalChange by thisChange
        totalChange += thisChange

        # check if thisChange is lower than minChange
        if thisChange < minChange[1]:
            # if so, update minChange with data from this row
            minChange = [thisDate, thisChange]
        # check if thisChange is higher than minChange
        if thisChange > maxChange[1]:
            # if so, update maxChange with data from this row
            maxChange = [thisDate, thisChange]
        # set previousPL as thisPL before looping back to next row
        previousPL = thisPL

# ------- close file stream --------
print("\n\n")
# average change is totalChange divided by totalMonths-1
# (because no change for first month)
# round to 2 decimal places
averageChange = round(totalChange / (totalMonths - 1), 2)

# we now have all necessary values, so we format the output in a string
outputS = f"Financial Analysis\n\n------------------------\n\nTotal Months: {totalMonths}\n\nTotal: {totalPL}\n\nAverange Change: {averageChange}\n\nGreatest Increase in Profits: {maxChange[0]} ({maxChange[1]})\n\nGreatest Decrease in Profits: {minChange[0]} ({minChange[1]})"

# write output to file


# print output to console
print(outputS)
