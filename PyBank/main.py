# UofT SCS EdX Data Bootcamp
# Challenge 3. Part 1: PyBank
# Script Author: Tania Barrera (tsbarr)
# -----------------------------------------

# import modules
import os
import csv

# --- variables that will store output
# month count
totalMonths = 0
# sum all profit/losses (PL)
totalPL = 0
# change = previousPL - currentPL
# sum all changes in PL, to calculate average change later
totalChange = 0
# dictionary to store data on greatest changes (decrease and increase)
greatest = {
    "decrease" : ["", 0],   # [date, value]
    "increase" : ["", 0]    # [date, value]
}

# --- read input
# input source path
inPath = os.path.join('resources', 'budget_data.csv')

# ------- open file stream --------
# open input csv file using path
with open(inPath) as inFile:
    # csv reader, columns: date, change
    inReader = csv.reader(inFile, delimiter=',')

    # store header row
    headers = next(inReader)

    # get first row before itaring
    # because we are not calculating change for it
    # but we need it to calculate the first change
    firstRow = next(inReader)
    # count first month and profit/losses
    totalMonths = 1
    totalPL = int(firstRow[1])  # cast str to int
    # set previousPL to profit/losses of first month
    previousPL = int(firstRow[1])  # cast str to int

    # iterate through rest of rows
    for row in inReader:
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

        # check if thisChange is lower than the greatest decrease
        if thisChange < greatest["decrease"][1]:
            # if so, update minChange with data from this row
            greatest["decrease"] = [thisDate, thisChange]
        # check if thisChange is higher than minChange
        if thisChange > greatest["increase"][1]:
            # if so, update maxChange with data from this row
            greatest["increase"] = [thisDate, thisChange]
        # set previousPL as thisPL before looping back to next row
        previousPL = thisPL
# ------- close file stream --------

# --- average change
# totalChange divided by totalMonths-1
# (because no change for first month)
# round to 2 decimal places
averageChange = round(totalChange / (totalMonths - 1), 2)

# --- format the output in a string
outString = f"\
Financial Analysis\n\n\
----------------------------\n\n\
Total Months: {totalMonths}\n\n\
Total: ${totalPL}\n\n\
Averange Change: ${averageChange}\n\n\
Greatest Increase in Profits: {greatest['increase'][0]} (${greatest['increase'][1]})\n\
Greatest Decrease in Profits: {greatest['decrease'][0]} (${greatest['decrease'][1]})\
"

# --- write output to file
# output source path
outPath = os.path.join('analysis', 'budget_analysis_results.txt')

# ------- open file stream --------
# open output txt file using path
with open(outPath, mode="w") as outFile:
    outFile.write(outString)
# ------- close file stream --------

# --- print output to console
print("\n\n")
print(outString)
print("\n\n")

# THE END
