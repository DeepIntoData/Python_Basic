import os
import csv  

os.chdir(os.path.dirname(os.path.abspath(__file__))) # set directory to the files we want
#print(os.getcwd()) #test

# Join csv 
csvpath = os.path.join('Resources', 'election_data.csv') # csv file assigned to csv variable

# CSV Reader
with open(csvpath) as csvfile: # with every opening of the .csv file, set it as a csvfile type
   
    csvreader = csv.reader(csvfile, delimiter=',')  # csvreader is just a variable to hold the split segments of the csvfile, specified by delimiter. Open the csv file in notepad to see delimiter. This is seperate by a ,
    
    next(csvreader) #Skip header

    # Declare Variable
    totv=0      # Total Votes
    tot=0       # Total P/L
    avg=0       # Average Change
    KhanC = 0
    CorreyC = 0
    LiC = 0
    OTooleyC = 0
    Winner_Vote = 0

    # Row Calculations 
    for row in csvreader:     
        
        #month counter
        totv = totv + 1 

        if row[2] == "Khan":
            KhanC += 1
            KC = str(KhanC)
        elif row[2] == "Correy":
            CorreyC += 1
        elif row[2] == "Li":
            LiC += 1
        elif row[2] == "O'Tooley":   
            OTooleyC += 1

    K = round((KhanC/totv)*100,2)
    C = round((CorreyC/totv)*100,2)
    L = round((LiC/totv)*100,2)
    O = round((OTooleyC/totv)*100,2)
         
    if KhanC > Winner_Vote:
        winner = "Khan"
    elif CorreyC > Winner_Vote:
        winner = "Correy"
    elif LiC > Winner_Vote:
        winner = "Li"
    elif OTooleyC > Winner_Vote:
        winner = "O'Tooley"

#Results
print ("")
print("Election Results")
print("----------------------------------------")
print("Total Votes: " + str(totv))
print("----------------------------------------")
print(f"Khan: {K}% ({(KhanC)})")
print(f"Correy: {C}% ({(CorreyC)})")
print(f"Li: {L}% ({(LiC)})")
print(f"O'Tooley: {O}% ({(OTooleyC)})")
print("----------------------------------------")
print(f"Winner: {winner}")
print("----------------------------------------")
print(" ")

# Specify the file to write to
output_path = os.path.join("Analysis", "FinalAnalysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as text:

    text.write("Election Results\n")
    text.write("----------------------------------------\n")
    text.write("Total Votes: " + str(totv) +"\n")
    text.write("----------------------------------------\n")
    text.write(f"Khan: {K}% ({(KhanC)})\n")
    text.write(f"Correy: {C}% ({(CorreyC)})\n")
    text.write(f"Li: {L}% ({(LiC)})\n")
    text.write(f"O'Tooley: {O}% ({(OTooleyC)})\n")
    text.write("----------------------------------------\n")
    text.write(f"Winner: {winner}\n")
    text.write("----------------------------------------\n")
