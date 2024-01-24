import os
import csv

#path for csv file
csvpath = os.path.join("Resources", "budget_data.csv")
data = []

#This is opening the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#This part is to code can skip over the headers
    next(csvreader)
#inputting data into the list
    for row in csvreader:
        date = (row[0])
        profit = (row[1])
        data.append((date, float(profit)))
changes = []
previous_profit = data[0][1]
total = previous_profit

#steps through each row, issue to solve is that previous profit needs to be remembered for calculations, this is that process. 
for i in range(1,len(data)):
    current_profit = data[i][1]
    change = current_profit - previous_profit
#tracking changes for calculations
    changes.append(change)
    previous_profit = current_profit
    total += current_profit


#Calculations for for printing and exporting 
average_change = sum(changes) / len(changes)
maxchange = max(changes) 
minchange = min(changes)
maxchange_index= changes.index(maxchange)
minchange_index= changes.index(minchange)
#grabbing dates, has to be + 1 to be correct
maxchange_date = data[maxchange_index + 1][0]
minchange_date = data[minchange_index + 1][0]

#Print Statements for Terminal
print(f"Total Months:{len(data)}")
print(f"Net Profit: ${round(total)}")
print(f"Average change: ${round(average_change,2)}")
print(f"Min Change: {minchange_date} ${round(minchange)}")
print(f"Max Change: {maxchange_date} ${round(maxchange)}")

#this is the Output to the text file
output_path = os.path.join("Analysis","BankResults.txt")
with open(output_path, "w") as text:
    text.write("Financial Analysis")
    text.write("\n""__________________________________________________________""\n")
    text.write(f"Total Months:{len(data)}")
    text.write("\n""__________________________________________________________""\n")
    text.write(f"Net Profit: ${round(total)}")
    text.write("\n""__________________________________________________________""\n")
    text.write(f"Average change: ${round(average_change,2)}")
    text.write("\n""__________________________________________________________""\n")
    text.write(f"Min Change: {minchange_date} ${round(minchange)}")
    text.write("\n""__________________________________________________________""\n")
    text.write(f"Max Change: {maxchange_date} ${round(maxchange)}")
