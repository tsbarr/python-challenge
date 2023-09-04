# Python Challenge: PyBank and PyPoll

**Student name:** Tania Barrera

---

This repo contains my work for the third weekly challenge of the UofT SCS edX Data Bootcamp.

This challenge contains two parts: PyBank and PyPoll. Each part is contained within its own folder and should be run within that folder (i.e. PyBank or PyPoll), as each program is independent from each other. The scripts named `main.py` will read in the input data assuming that they are being run within the PyBank or PyPoll subfolder and use this assumption to assign the file paths.

## PyBank

### Instructions

In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company.

You will be given a financial dataset called `budget_data.csv`. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

- The total number of months included in the dataset

- The net total amount of "Profit/Losses" over the entire period

- The changes in "Profit/Losses" over the entire period, and then the average of those changes

- The greatest increase in profits (date and amount) over the entire period

- The greatest decrease in profits (date and amount) over the entire period

In addition, your final script should both print the analysis to the terminal and export a text file with the results.

### Running the program

Run [`main.py`](PyBank/main.py) within the PyBank folder. The input file path for the program is [`/resources/budget_data.csv`](PyBank/resources/budget_data.csv) and the output file path is [`/analysis/budget_analysis_results.txt`](PyBank/analysis/budget_analysis_results.txt). It is very important to make sure to navigate to the PyBank folder before running `main.py`, so these file paths work as intended.

### Imports

The modules imported for this program are:

- **`os`:** to make the file paths compatible between different operating systems.

- **`csv`:** to read the input data from the csv file, splitting the data columns using the comma delimiter.

### Output calculation

The values in the output are both printed in the terminal and stored in an output analysis text file. Here is a short description of how they are calculated:

- **Total months:** 
    
    - Count every data row, since each row contains one month's data.

- **Total Profit/Losses:** 
    
    - Sum all monthly amounts from the second data column.

- **Average Change:** 

    - Get every month's change as the difference between the profit/losses of that month and the profit/losses of the previous month.
        - *Note:* The first month has no change, since there is no previous month for it.
    
    - Sum all monthly changes.
    
    - Divide the sum by the total number of months minus 1, to account for the lack of change in the first month.

    - It is formatted to 2 decimal spaces using the f-string formatting `:.2f`

- **Greatest increase in profits:**

    - Compare the monthly changes and get the maximum one and the date when it happens.

- **Greatest decrease in profits:**

    - Compare the monthly changes and get the minimum one and the date when it happens.

### References

Some code sections were adapted from the UofT SCS EdX Data Bootcamp class activities.

Challenge instructions and input file:

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.



## PyPoll

### Instructions

In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

You will be given a set of poll data called `election_data.csv`. The dataset is composed of three columns: "Voter ID", "County", and "Candidate".

Your task is to create a Python script that analyzes the votes and calculates each of the following values:

- The total number of votes cast

- A complete list of candidates who received votes

- The percentage of votes each candidate won

- The total number of votes each candidate won

- The winner of the election based on popular vote

In addition, your final script should both print the analysis to the terminal and export a text file with the results.

### Running the program

Run [`main.py`](PyPoll/main.py) within the PyPoll folder. The input file path for the program is [`/resources/election_data.csv`](PyPoll/resources/election_data.csv) and the output file path is [`/analysis/election_analysis_results.txt`](PyPoll/analysis/election_analysis_results.txt). It is very important to make sure to navigate to the PyPoll folder before running before running `main.py`, so these file paths work as intended.

### Imports

The modules imported for this program are:

- **`os`:** to make the file paths compatible between different operating systems.

- **`csv`:** to read the input data from the csv file, splitting the data columns using the comma delimiter.

In addition, the dictionary subclass **`Counter`** from the **`collections`** module is also imported. Is is used as the data structure that performs and stores each candidate's vote count. The subclass Counter has the methods `.most_common()` and `.total()` were used as well to determine the winner and calculate the total number of votes, respectively (details below).

### Output calculation

The values in the output are both printed in the terminal and stored in an output analysis text file. They were calculated using a `Counter`, which is a subclass of dictionary.

Each row in the input containes information about a single vote. The third column gives us for what candidate each vote was. So, I extracted the third column using a List Comprehension and used it as an argument for `Counter()`, which counts how many times each candidate name appears in the column and returns a dictionary with keys corresponding to the names and values corresponding to this vote count for each candidate.

Once this Counter dictionary was generated, I used it to calculate the rest of the output values. Here is a short description of how they are calculated:

- **Total votes:** 
    
    - Used the Counter method `.total()`, which sums all counts in the Counter dictionary.

- **Individual candidate summary:** 
    
    - Looped through the `Counter` dictionary to get data for every candidate that received votes:

        - name: the key

        - total number of votes: the count value
        
        - percentage of votes: count value / total votes. It is formatted as a percentage with 3 decimals using the f-string formatting `:.3%`

- **Winner:** 
    
    - Used the Counter method `.most_common(n)`, with `n=1`, which returns a list of lists with each internal lists being the pairs `[key, value]` of each of the top `n` items with the highest counts.
        - *Note:* Currently, the program cannot deal with ties. It will only return the first name that has the highest count, ignoring any other name that comes afterwards that has the same vote count. However, the `.most_common(n)` method can be used to modify the program to determine if there are ties (e.g. with a loop where `n` increases until the vote count is different from when `n=1`).

### References

Some code sections were adapted from the UofT SCS EdX Data Bootcamp class activities.

Challenge instructions and input file:

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.

Other code sections were adapted from other sources, specific explanations are found within the script comments:

| Purpose                            	| URL                                      	|
|------------------------------------	|------------------------------------------	|
| `Counter` subclass documentation 	| https://docs.python.org/3/library/collections.html#collections.Counter 	|
| How to use the Counter subclass within a file reader `with` statement. "Counting Files by Type" example	| https://realpython.com/python-counter/	|
| `.most_common(n)` methods documentation	| https://docs.python.org/3/library/collections.html#collections.Counter.most_common	|
