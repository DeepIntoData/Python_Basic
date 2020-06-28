import os
import csv  

os.chdir(os.path.dirname(os.path.abspath(__file__))) # set directory to the files we want
#print(os.getcwd()) #test

# Join csv 
csvpath = os.path.join('Resources', 'budget_data.csv') # csv file assigned to csv variable

# CSV Reader
with open(csvpath) as csvfile: # with every opening of the .csv file, set it as a csvfile type
   
    csvreader = csv.reader(csvfile, delimiter=',')  # csvreader is just a variable to hold the split segments of the csvfile, specified by delimiter. Open the csv file in notepad to see delimiter. This is seperate by a ,
    
    next(csvreader) #Skip header

    # Declare Variable
    totm=0      # Total Months
    tot=0       # Total P/L
    avg=0       # Average Change
    a = 0       # Previous Row
    b = 0       # Current Row
    c = 0       # Total Change Value
    d = 0       # Row Change Value
    max_a = 0   # Max Value of Row Change Value
    min_a = 0   # Min Value of Row Change Value

    # Row Calculations 
    for row in csvreader:     
        
        #month counter
        totm = totm + 1    

        #total counter
        tot = tot + int(row[1])
        #tot = row[1]

        b=int(row[1]) #hold value of current row[1]

        #change avg calc
        if totm > 1: #skip a row
            d = b - a #difference between consecutive rows 
            c = c + d #differences added up 
        a = b  #pass to the next row

        if d > max_a:   #compares change values and stores greatest
            max_a = d   
            mx = row[0] #keep row
        if d < min_a:
            min_a = d
            mn = row[0]

    avg = c/(totm-1) #count only the rows that have a previous

#Results
print("")
print("Financial Analysis")
print("----------------------------------------")
print("Total Months: " + str(totm))
print("Total: " + "$" + str(tot))
print("Average Change : $" + str(round(avg,2)))
print("Greatest Increase in Profits: " + str(mx) + " ($" + str(max_a) + ")")
print("Greatest Decrease in Profits: " + str(mn) + " ($" + str(min_a) + ")")
print("----------------------------------------")
print("")

# Specify the file to write to
output_path = os.path.join("Analysis", "FinalAnalysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as text:

    text.write("Financial Analysis\n")
    text.write("----------------------------------------\n")
    text.write("Total Months: " + str(totm) +"\n")
    text.write("Total: " + "$" + str(tot)+"\n")
    text.write("Average Change : $" + str(round(avg,2))+"\n")
    text.write("Greatest Increase in Profits: " + str(mx) + " ($" + str(max_a) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(mn) + " ($" + str(min_a) + ")\n")
    text.write("----------------------------------------\n")


