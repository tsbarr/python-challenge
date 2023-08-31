# UofT SCS EdX Data Bootcamp
# Challenge 3. Part 2: PyPoll
# Script Author: Tania Barrera (tsbarr)
# -----------------------------------------

# import modules
import os
import csv

# --- variables that will store output
# a dictionary with key = candidate, value = voteCount
votesByCandidate = {}
# sum of vote counts
totalVotes = 0
# string to concatenate the portion of the output for individual candidates
outCandidateInfo = ""

# --- read input
# input source path
ipath = os.path.join('resources', 'election_data.csv')

# ------- open file stream --------
# open input csv file using path
with open(ipath) as ifile:
    # csv reader, columns: id, county, candidate
    ireader = csv.reader(ifile, delimiter=',')

    # skip headers
    next(ireader)

    # iterate through rest of rows
    for row in ireader:
        # get name of candidate in the row
        thisCandidate = row[2]
        # if thisCandidate exists in votesByCandidate
        # https://flexiple.com/python/check-if-key-exists-in-dictionary-python/
        if thisCandidate in votesByCandidate:
            # increase thisCandidate voteCount by 1
            votesByCandidate[thisCandidate] += 1
        else:
            # add it and set to 1
            # https://www.w3schools.com/python/python_dictionaries_add.asp
            votesByCandidate[thisCandidate] = 1
# ------- close file stream --------

# use max() with key argument to find winner
# parameter iterable: candidate names (the keys of the dict votesByCandidate)
# key argument: lambda function that returns the candidate 'voteCount'
# therefore, the voteCount will be used to sort and it will return the name with the highest voteCount
# max function documentation: https://thepythonguru.com/python-builtin-functions/max/
# how to lambda functions: https://www.w3schools.com/python/python_lambda.asp
winner = max(votesByCandidate.keys(), key=lambda name: votesByCandidate[name])

# --- totalVotes
# iterate through candidates in votesByCandidate
for thisCandidate in votesByCandidate:
    # add the voteCount of each candidate to totalVotes
    totalVotes += votesByCandidate[thisCandidate]


# --- percentOfVote and output for individual candidates
# now that we have the totalVotes, we can calculate percentOfVote
# and format the candidate-level output, concatenating them in outCandidateInfo
for thisCandidate in votesByCandidate:
    # percentOfVote = voteCount / totalVotes, not necessary to store long-term
    percentOfVotes = votesByCandidate[thisCandidate] / totalVotes
    # format and add thisCandidate info to output string
    outCandidateInfo += f"{thisCandidate}: {round(percentOfVotes*100, 3)}% ({votesByCandidate[thisCandidate]})\n\n"

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
