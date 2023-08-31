# UofT SCS EdX Data Bootcamp
# Challenge 3. Part 2: PyPoll
# Script Author: Tania Barrera (tsbarr)
# -----------------------------------------

# --- import modules
import os
import csv
# used to count votes
# documentation: https://docs.python.org/3/library/collections.html#collections.Counter
from collections import Counter

# --- read input
# input source path
ipath = os.path.join('resources', 'election_data.csv')

# ------- open file stream --------
# open input csv file using path
with open(ipath) as ifile:
    # csv reader, columns: id, county, candidate
    ireader = csv.reader(ifile, delimiter=',')

    # store header row
    header = next(ireader)

    # using the rest of the rows in ireader,
    # extract the column of candidate names into a tuple
    # and use Counter() to count the instances of each name
    # voteCounts is now a dict with keys = candidate names, values = vote count
    # Based on "Counting Files by Type" example at: https://realpython.com/python-counter/
    voteCounts = Counter((row[2] for row in ireader))
# ------- close file stream --------

# use max() with key argument to find winner
# parameter iterable: candidate names (the keys of the dict votesByCandidate)
# key argument: lambda function that returns the candidate 'voteCount'
# therefore, the voteCount will be used to sort and it will return the name with the highest voteCount
# explanation of max's key argument: https://thepythonguru.com/python-builtin-functions/max/
# how to lambda functions: https://www.w3schools.com/python/python_lambda.asp
winner = max(voteCounts.keys(), key=lambda name: voteCounts[name])
# note: in case of tie, it will just return the first name that has the max count,
# see bottom of script for a way to detect if there are ties

# --- totalVotes
# use method .total from Counter subclass to sum all counts
totalVotes = voteCounts.total()

# --- percentOfVote and output for individual candidates
# now that we have the totalVotes, we can calculate percentOfVote
# and format the candidate-level output, concatenating them in oCandidateInfo
oCandidateInfo = ""
for name in voteCounts:
    # percentOfVote = voteCount / totalVotes, not necessary to store long-term
    # multiply by 100 and round to 3 decimal places
    percentOfVotes = round(voteCounts[name] / totalVotes * 100, 3)
    # format and add this candidate's info to output string
    oCandidateInfo += f"{name}: {percentOfVotes}% ({voteCounts[name]})\n\n"

# --- format the whole output, store it in outString
oString = f"\
Election Results\n\n\
-------------------------\n\n\
Total Votes: {totalVotes}\n\n\
-------------------------\n\n\
{oCandidateInfo}\
-------------------------\n\n\
Winner: {winner}\n\n\
-------------------------\
"

# --- write output to file
# output source path
opath = os.path.join('analysis', 'election_analysis_tsbarr.txt')

# ------- open file stream --------
# open output txt file using path
with open(opath, mode="w") as ofile:
    # write output string to file
    ofile.write(oString)
# ------- close file stream --------

# --- print output to console
print("\n\n")
print(oString)
print("\n\n")

# THE END
# --------------------------------------------------------------------------------------------

# EXTRA: check for ties
# count how many times voteCount values appear
# find max voteCount
# look at the value of max voteCount in second count
# if it is more than 1, it is not unique
# therefore, there is a tie
# if Counter(voteCounts.values())[max(voteCounts.values())] > 1:
#     print(f"WARNING! There is at tie. {winner} is not the only winner. Revote time.")
