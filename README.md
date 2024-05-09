# python-challenge

There are 2 projects within this challenge.  The first is an analysis of profit/loss for a bank with monthly data.  The code reads in the csv file, performs calculations and transformations with the data, and outputs a text file with the budget analysis.

The second project reads in a csv file with voting data for a precinct, transforms the data, sums the votes for each candidate and outputs a text file summarizing the performance of each candidate.  

A Jupyter notebook is used for each of these analyses.


The analysis folders contain python code in jupyter notebooks for the relevant file in the related Resources folder.

For each, the coder reads in the information from the cvs file, stores the information in lists, and performs calculations and analysis on the data.

The PyBank code outputs both to the terminal and to a text file which is named "budget_analysis.txt".
It shows the total number of months in the data, the total profit over the period, the average month to month change in profit, the largest increase in profits and the largest decrease in profits.

Data analysis - the total profit over the period is positive and more than ten times greater than any monthly increase or decrease in profits.  The average monthly change is negative.  This may be because there are more highly negative months than highly positive ones, despite the positive months totalling much more than the negatives. Even a month with a positive profit may have a negative CHANGE from the previous month.  It must be more common to have positive spikes in profits, with slow month to month declines in positive profits.  This would account for the positive total profit and the negative average change.

The PyPoll code outputs to both the terminal and to a text file, which is named "pollanalysis.txt"
It shows the total votes, the total votes and percentages for each candidate, and the name of the candidate who received the most votes.