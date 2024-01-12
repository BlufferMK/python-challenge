#pybank python code
import os
import csv


csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)


print("That didn't work.")

row_count = sum(1 for row in csvreader)

print(row_count)

