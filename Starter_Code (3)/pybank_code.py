#pybank python code
import os
import csv

csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
<<<<<<< HEAD
    print(csvreader)

    row_count = sum(1 for row in csvreader)

    for row in csvreader:
        print(row)
    
return    
    #print(row_count)
    #print("There are ", row_count, "rows.")
=======
    print(csvreader)
>>>>>>> bead1db62540251c1f7474d3fe4b0bf3ef63d872
