import os
import csv

csvpath = os.path.join('.', 'budget_data.csv')

with open(csvpath, newline= '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #reads the first line of the file which is the header and we stored it in the csv_header variable.
    csv_header = next(csvreader)

    #variables needed
    counter = 0
    moneyz = 0
    oldAvg = 0
    newAvg = 0
    totalAvg = 0
    currHigh = 0
    currLow = 0
    tempAvg = 0

    #goes through each row in the CSV file so we can read it and do whatever we want with it
    for row in csvreader:
        if (counter != 0):
            newAvg = float(row[1])
            totalAvg += newAvg - oldAvg
            tempAvg = newAvg - oldAvg
            #Stores Highest Avg
        if currHigh < tempAvg:
            highestDate = str(row[0])
            currHigh =  tempAvg
            #Stores Lowest Avg
        if currLow > tempAvg:
            lowestDate = str(row[0])
            currLow =  tempAvg
        oldAvg = float(row[1])
        #Sums up our Total $
        moneyz += int(row[1])
        #Counts the rows of months in data
        counter = counter + 1

    #Calculate average so we can print it
    averageChange= totalAvg / (counter - 1)

    #Displays results
    print("Financial Analysis")
    print("------------------------------")
    print(f"Total Months: {counter}")
    print(f"Total: ${moneyz}")
    print(f"Average Change: ${round(averageChange,2)}")
    print(f"Greatest Increase in Profits: {highestDate} (${int(currHigh)})")
    print(f"Greatest Decrease in Profits: {lowestDate} (${int(currLow)})")

