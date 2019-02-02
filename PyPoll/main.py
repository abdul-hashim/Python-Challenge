import os
import csv

#csvpath = os.path.join('.', 'election_data.csv')
csvpath = os.path.join('.', 'testt.csv')

with open(csvpath, newline= '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #reads the first line of the file which is the header and we stored it in the csv_header variable.
    csv_header = next(csvreader)

    countTotal = 0
    countKhan = 0
    countCorrey = 0
    countLi = 0
    countOTooley = 0
    currentMax = 0

    for row in csvreader:
        #Checks if its Khan
        if row[2] == "Khan":
            #Adds Khan to a counter to track him
            countKhan = countKhan + 1
            #Checks if Khan has the most votes and if he does then adds his name as the winner
            if currentMax < countKhan:
                currentMax = countKhan
                winner = "Khan"
        elif row[2] == "Correy":
            countCorrey = countCorrey + 1
            if currentMax < countCorrey:
                currentMax = countCorrey
                winner = "Correy"
        elif row[2] == "Li":
            countLi = countLi + 1
            if currentMax < countLi:
                currentMax = countLi
                winner = "Li"
        elif row[2] == "O'Tooley":
            countOTooley = countOTooley + 1
            if currentMax < countOTooley:
                currentMax = countOTooley
                winner = "O'Tooley"


    #adds total count
    countTotal = countKhan + countCorrey + countLi + countOTooley

    #Print out the results
    print(f"Election Results")
    print(f"---------------------------")
    print(f"Total Votes: {countTotal}")
    print(f"---------------------------")
    print(f"Khan: {round(countKhan/countTotal * 100, 3)}% ({countKhan})")
    print(f"Correy: {round(countCorrey/countTotal *100, 3)}% ({countCorrey})")
    print(f"Li: {round(countLi/countTotal * 100, 3)}% ({countLi})")
    print(f"O'Tooley: {round(countOTooley/countTotal*100, 3)}% ({countOTooley})")
    print(f"---------------------------")
    print(f"The Winner is: {winner}!")
    print(f"---------------------------")