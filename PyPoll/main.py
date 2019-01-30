import os
import csv

csvpath = os.path.join('.', 'election_data.csv')

with open(csvpath, newline= '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #reads the first line of the file which is the header and we stored it in the csv_header variable.
    csv_header = next(csvreader)
    counter = 0
    for row in csvreader:
        counter = counter + 1
        if counter < 10:
            print(f"{row}")