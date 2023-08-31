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
# max function documentation: https://thepythonguru.com/python-builtin-functions/max/
# how to lambda functions: https://www.w3schools.com/python/python_lambda.asp
winner = max(voteCounts.keys(), key=lambda name: voteCounts[name])

# --- totalVotes
# sum of values in voteCounts
totalVotes = 0
# iterate through candidates in votesByCandidate
for thisCandidate in voteCounts:
    # add the voteCount of each candidate to totalVotes
    totalVotes += voteCounts[thisCandidate]


# --- percentOfVote and output for individual candidates
# now that we have the totalVotes, we can calculate percentOfVote
# and format the candidate-level output, concatenating them in outCandidateInfo
outCandidateInfo = ""
for thisCandidate in voteCounts:
    # percentOfVote = voteCount / totalVotes, not necessary to store long-term
    percentOfVotes = voteCounts[thisCandidate] / totalVotes
    # format and add thisCandidate info to output string
    outCandidateInfo += f"{thisCandidate}: {round(percentOfVotes*100, 3)}% ({voteCounts[thisCandidate]})\n\n"

# --- format the whole output, store it in outString
outString = f"\
Election Results\n\n\
-------------------------\n\n\
Total Votes: {totalVotes}\n\n\
-------------------------\n\n\
{outCandidateInfo}\
-------------------------\n\n\
Winner: {winner}\n\n\
-------------------------\
"

# # --- write output to file
# # output source path
# outPath = os.path.join('analysis', 'election_analysis_tsbarr.txt')

# # ------- open file stream --------
# # open output txt file using path
# with open(outPath, mode="w") as outFile:
#     outFile.write(outString)
# # ------- close file stream --------

# --- print output to console
print("\n\n")
print(outString)
print("\n\n")

# THE END
