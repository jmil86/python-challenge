# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

#get current working directory to make sure the files are present
print(os.getcwd())

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
# Add more variables to track other necessary financial data
total_value = 0
largest_loss = float('inf')
largest_loss_month = ""
largest_gain = float('-inf')
largest_gain_month = ""
average_change = 0
net_change_list = []
previous_value = 0

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)
    # Extract first row to avoid appending to net_change_list
    print(f"CSV Header: {header}")

    # Track the total and net change
    first_data = next(reader)
    total_value = int(first_data[1])
    total_months += 1
    previous_value = int(first_data[1])

    # Process each row of data
    for row in reader:

        #count the months
        total_months = total_months + 1

        # Track the total
        total_value += int(row[1])

        # Track the net change
        net_change = int(row[1]) - previous_value
        net_change_list.append(net_change)
        previous_value = int(row[1])

        # Calculate the greatest increase in profits (month and amount)
        if net_change > largest_gain:
            largest_gain = net_change
            largest_gain_month = row[0]

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < largest_loss:
            largest_loss = net_change
            largest_loss_month = row[0]

# Calculate the average net change across the months, the changes happen over one less month than the total months
average_change = sum(net_change_list) / (total_months - 1)

# Generate the output summary
print(f"Financial Analysis")
print(f"-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_value}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {largest_gain_month} (${largest_gain})")
print(f"Greatest Decrease in Profits: {largest_loss_month} (${largest_loss})")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:

    txt_file.write(f"Financial Analysis\n")
    txt_file.write(f"--------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total Ending Value: ${total_value}\n")
    txt_file.write(f"Average Change: {average_change:.2f}\n")
    txt_file.write(f"Greatest Profit (Month / Amount): {largest_gain_month} (${largest_gain})\n")
    txt_file.write(f"Lowest Profit (Month / Amount): {largest_loss_month} (${largest_loss})\n")