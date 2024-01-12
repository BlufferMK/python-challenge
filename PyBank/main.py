import os
os.getcwd()

import csv

file ='c:/Users/mrkol/Documents/BootcampData2023/python-challenge/PyBank/Resources/budget_data.csv'


#csvpath = os.path.join('C:\Users\mrkol\Documents\BootcampData2023\python-challenge\PyBank\Resources\budget_data.csv')

with open(file) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter= ',')

    list_of_column_names = []
    for row in csvreader:
        list_of_column_names.append(row)
        break

print("List of column names : ", list_of_column_names[0])

