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
inPath = os.path.join('resources', 'election_data.csv')

# ------- open file stream --------
# open input csv file using path
with open(inPath) as inFile:
    # csv reader, columns: id, county, candidate
    inReader = csv.reader(inFile, delimiter=',')

    # store header row
    header = next(inReader)

    # using the rest of the rows in ireader,
    # extract the column of candidate names into a tuple
    # and use Counter() to count the instances of each name
    # voteCounts is now a dict with keys = candidate names, values = vote count
    # Based on "Counting Files by Type" example at: https://realpython.com/python-counter/
    voteCounts = Counter((row[2] for row in inReader))
# ------- close file stream --------

# --- winner
# use method .most_common(n) from Counter subclass to find the winner
# it returns a list of tuples with the top n highest keys and their counts
# doc: https://docs.python.org/3/library/collections.html#collections.Counter.most_common
# in this case, we use it with n=1
# and extract the name as the first item of the first tuple in the list
# note: it can be adapted to detect ties if we use a higher n and compare results
# as is, in case of tie, it will just return the name that appears first that has the max count
winner = voteCounts.most_common(1)[0][0]

# --- totalVotes
# use method .total from Counter subclass to sum all counts
totalVotes = voteCounts.total()

# --- percentOfVote and output for individual candidates
# now that we have the totalVotes, we can calculate percentOfVote
# and format the candidate-level output, concatenating them in candidateSummary
candidateSummary = ""
for name in voteCounts:
    # percentOfVote = voteCount / totalVotes, 
    # not necessary to store after the loop
    percentOfVotes = voteCounts[name] / totalVotes
    # format and add this candidate's info to output string
    # percentOfVotes is formatted as percent with 3 decimals using f-string formatting
    candidateSummary += f"{name}: {percentOfVotes:.3%} ({voteCounts[name]})\n\n"

# --- format the whole output, store it in outString
outString = f"\
Election Results\n\n\
-------------------------\n\n\
Total Votes: {totalVotes}\n\n\
-------------------------\n\n\
{candidateSummary}\
-------------------------\n\n\
Winner: {winner}\n\n\
-------------------------\
"

# --- write output to file
# output source path
outPath = os.path.join('analysis', 'election_analysis_tsbarr.txt')

# ------- open file stream --------
# open output txt file using path
with open(outPath, mode="w") as outFile:
    # write output string to file
    outFile.write(outString)
# ------- close file stream --------

# --- print output to console
print("\n\n")
print(outString)
print("\n\n")

# THE END
