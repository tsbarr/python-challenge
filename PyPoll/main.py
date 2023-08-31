# UofT SCS EdX Data Bootcamp
# Challenge 3. Part 2: PyPoll
# Script Author: Tania Barrera (tsbarr)
# -----------------------------------------

# import modules
import os
import csv

# --- variables that will store output
# a nested dictionary with key = candidate, value = dict{voteCount, percentOfVote}
# https://www.w3schools.com/python/python_dictionaries_nested.asp
candidateInfo = {}
# sum of vote counts
totalVotes = 0
# candidate with the max voteCount. dictionary with {name, voteCount}
winner = {"name": "", "voteCount": 0}
# string to concatenate the portion of the output for individual candidates
outIndividualCandidates = ""

# --- read input
# input source path
csvpath = os.path.join('resources', 'election_data.csv')

# ------- open file stream --------
# open input csv file using path
with open(csvpath) as csvfile:
    # csv reader, columns: id, county, candidate
    csvreader = csv.reader(csvfile, delimiter=',')

    # get headers
    headers = next(csvreader)

    # iterate through rest of rows
    for row in csvreader:
        # get name of candidate in the row
        thisCandidate = row[2]
        # if thisCandidate exists in candidateInfo
        # https://flexiple.com/python/check-if-key-exists-in-dictionary-python/
        if thisCandidate in candidateInfo:
            # increase thisCandidate voteCount by 1
            candidateInfo[thisCandidate]["voteCount"] += 1
        else:
            # add it and set voteCount to 1
            # https://www.w3schools.com/python/python_dictionaries_add.asp
            candidateInfo[thisCandidate] = {"voteCount": 1}
        # winner calculation:
        # check if candidate name is different from winner AND count is higher
            # note: final voteCount in winner dict wont match the actual voteCount,
            # but this way it wont update each time a vote is count for current winner
            # TODO: handle ties, not necessary for current challenge
        if winner["name"] != thisCandidate and candidateInfo[thisCandidate]["voteCount"] > winner["voteCount"]:
            print(f"\n\n---Update winner:---\n\tFormer:\t{winner}\n")
            # update with thisCandidate values
            winner = {
                "name": thisCandidate,
                "voteCount": candidateInfo[thisCandidate]["voteCount"]
            }
            print(f"\tNew:\t{winner}")
# ------- close file stream --------

# --- totalVotes
# iterate through candidates in candidateInfo
for thisCandidate in candidateInfo:
    # add the voteCount of each candidate to totalVotes
    totalVotes += candidateInfo[thisCandidate]["voteCount"]


# --- percentOfVote
# now that we have the totalVotes, we can calculate percentOfVote
# and format the candidate-level output, concatenating them in outIndividualCandidates
for thisCandidate in candidateInfo:
    # add percentOfVote to candidate entry,
    # as voteCount / totalVotes
    candidateInfo[thisCandidate]["percentOfVotes"] = candidateInfo[thisCandidate]["voteCount"] / totalVotes
    # format and add thisCandidate info to output string outIndividualCandidates
    outIndividualCandidates = outIndividualCandidates + \
        f"{thisCandidate}: {round(candidateInfo[thisCandidate]['percentOfVotes']*100, 3)}% ({candidateInfo[thisCandidate]['voteCount']})\n\n"

# --- format the whole output, store it in a string
outString = f"Election Results\n\n-------------------------\n\nTotal Votes: {totalVotes}\n\n-------------------------\n\n{outIndividualCandidates}-------------------------\n\nWinner: {winner['name']}\n\n-------------------------"

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
