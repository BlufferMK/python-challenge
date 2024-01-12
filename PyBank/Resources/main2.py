import os
import csv
file = open(budget_data.csv)
type(file)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
header
rows = []
for row in csvreader:
    rows.append(row)
    row
file.close()