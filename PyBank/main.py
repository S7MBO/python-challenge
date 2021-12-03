# File main.py

# Import modules
import os
import csv

# Set parameters of the variables
total_months = 0
net_total = 0
monthly_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999]

# Load the source file
source_file = os.path.join("Resources", "budget_data.csv")

# Open and Read CSV source file
with open(source_file) as financial_data:
    csvreader = csv.reader(financial_data)

    # Read header row first
    csvheader = next(csvreader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(csvreader)
    total_months += 1
    net_total += int(first_row[1])
    prev_net = int(first_row[1])

    for row in csvreader:

        # Track the total
        total_months += 1
        net_total += int(row[1])

        # Track the net change
        net_changes = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_changes]
        monthly_change += [row[0]]

        # Calculate the greatest increase
        if net_changes > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_changes

        # Calculate the greatest decrease
        if net_changes < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_changes

# Calculate the net change
net_monthly_average = sum(net_change_list) / len(net_change_list)

# Specify and word the exported information summary
export_summary = (
    f"Financial Analysis Report\n"
    f"\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average  Change: ${net_monthly_average:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Specify the exported file location
export_file = os.path.join("Analysis", "Budget_Analysis.txt")

# Print results to terminal
print(export_summary)

# Write to file and export
with open(export_file, "w") as txt_file:
    txt_file.write(export_summary)