#Reed Zimpfer
#Module 3 Challenge
#PyBank

import os
import csv

# Set path for accessing data and writing to output file
csvpath = os.path.join("Resources", "budget_data.csv")
output = os.path.join("analysis", "output.txt")

# Open the CSV
# Define variables "Profit/Losses" over the entire period = Revenue

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    month = []
    revenue = []
    net_change_list = []
    average_change = []

    # Loop through to fill month and revenue arrays
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    # Define month_count variable    
    month_count = len(month)
    # Define the net total amount of profit/losses as profit_sum variable
    revenue_count = map(int, revenue)
    profit_losses_sum = sum(revenue_count)

    # Add the individual net changes into the array net_change_list, then find the average (monthly) change
    for i in range(len(revenue) - 1):
        net_change = int(revenue[i+1]) - int(revenue[i])
        net_change_list.append(net_change)
    average_change = round(sum(net_change_list)/len(net_change_list), 2)
    
    #Greatest Increase in profits
    max_increase = max(net_change_list)
    #print(max_increase)
    k = net_change_list.index(max_increase)
    month_of_increase = month[k+1]

    #Greatest Decrease in profits
    max_decrease = min(net_change_list)
    #print(max_decrease)
    j = net_change_list.index(max_decrease)
    month_of_decrease = month[j+1]

    # Print statements to the terminal
    print(f"Financial Analysis")
    print(f"----------------------------------------------------" + "\n")
    print(f"Total Months: {month_count}")
    print(f"Net Total: ${profit_losses_sum}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {month_of_increase} (${max_increase})")
    print(f"Greatest Decrease in Profits: {month_of_decrease} (${max_decrease})")

# Write statements to the output file
with open(output,"w") as txt_file:
    txt_file.write(
        f"Financial Analysis\n"
        f"------------------------------------------------------\n"
        f"Total Months: {month_count}\n"
        f"Net Total: ${profit_losses_sum}\n"
        f"Average Change: ${average_change}\n"
        f"Greatest Increase in Profits: {month_of_increase} (${max_increase})\n"
        f"Greatest Decrease in Profits: {month_of_decrease} (${max_decrease})\n"
    )