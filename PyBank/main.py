# UofT SCS EdX Data Bootcamp 
# Challenge 3. Part 1: PyBank
# Script Author: Tania Barrera (tsbarr)
# -----------------------------------------

# import modules
import os
import csv

# input source path
csvpath = os.path.join('PyBank', 'resources', 'budget_data.csv')

# ------- opened --------
# open input csv file using path
with open(csvpath) as csvfile:
    	# csv reader
	csvreader = csv.reader(csvfile, delimiter=',')
	
	# get headers
	headers = next(csvreader())
	# first column: date
	# second column: change

	# initialize totalmonths and totalchange
	totalMonths = 0
	totalChange = 0

	# initialize vars to store min/max change and their dates
	minChangeValue = 0
	minChangeDate = ""
	maxChangeValue = 0
	maxChangeName = ""

	# iterate through all rows (except above headers)
	for row in csvreader:
		# get data from this row
		thisDate = row[1]
		thisChange = row[2]

		#increase totalMonths by 1
		totalMonths += 1

		# increase totalchange by thisChange
		totalChange += thisChange

		# check if thisChange is lower than minChange
		if thisChange < minChangeValue:
			# if so, update minChange variables
			minChangeValue = thisChange
			minChangeDate = thisDate
		
		# check if thisChange is higher than minChange
		if thisChange > maxChangeValue:
			# if so, update minChange variables
			maxChangeValue = thisChange
			maxChangeDate = thisDate

# ------- closed --------

# average change is totalChange / totalMonths
averageChange = totalChange / totalMonths

# we now have all necessary values, so we format the output in a string




		
print(f"---\n{csvreader.line_num}")


