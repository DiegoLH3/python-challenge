# csv is needed to be imported in order to start
import os
import csv

budget_data_path = os.path.join('/Users/diego/Desktop/python-challenge/PyBank/Resources/budget_data.csv')

with open(budget_data_path, 'r') as csvfile:

    csv_reader = csv.reader(csvfile)    
# header is used to read the headers of the list to use
    header = next(csv_reader)

# Creating the list of the headers
    Date = []
    Profit_Losses = []

    for row in csv_reader:
        Date.append(row[0])
        Profit_Losses.append(row[1])

# Creating a list for the Profit/Losses column
prof_loss = [int(value) for value in Profit_Losses]


tot_months = len(Date)

# We are adding up all the "Profit/Losses" column to get our total
total = sum(prof_loss) 

# Important because this is what creates the list of ALL the change in profit/losses
change = [prof_loss[i + 1] - prof_loss[i] for i in range(len(prof_loss) - 1)]

# Sum change is needed/used in order to add up all the change in profit
sum_change = sum(change)

# Average change
ave_change = round(sum_change / len(change), 2)

# Calculating for change in the Greatest Inc(Increase) in Profits
inc_change = max(change)

# Calculating for change in the Greatest Dec(Decrease) in Profits
dec_change = min(change)

# Dates for Greatest Inc(Increase) in Profits
inc_date = Date[change.index(inc_change) + 1]

# Dates for Greatest Dec(Decrease) in Profits
dec_date = Date[change.index(dec_change) + 1]


# Printed into Terminal
print_results = (
    "Financial Analysis\n"    
    "--------------------\n"
    f"Total Months: {tot_months}\n"
    f"Total: ${total}\n"
    f"Average Change: ${ave_change}\n"
    f"Greatest Inc in Profits: {inc_date}, (${inc_change})\n"
    f"Greatest Dec in Profits: {dec_date}, (${dec_change})\n"
)
print(print_results)

       

# Writes results to Text File
with open('/Users/diego/Desktop/python-challenge/PyBank/Analysis/Results', 'w') as fin_anal:
    fin_anal.write("Financial Analysis Results\n")
    fin_anal.write("--------------------\n")
    fin_anal.write(f"Total Months: {tot_months}\n")
    fin_anal.write(f"Total: ${total}\n")
    fin_anal.write(f"Average Change: ${ave_change}\n")
    fin_anal.write(f"Greatest Inc in Profits: {inc_date}, (${inc_change})\n")
    fin_anal.write(f"Greatest Dec in Profits: {dec_date}, (${dec_change})\n")

