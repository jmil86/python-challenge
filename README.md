# python-challenge

#### This is a description of each line of the PyPoll main.py code ####

# Import necessary modules
import csv
import os
## Imports the csv and os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path
## variables are defined to specify the file paths for input and output.


# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
## Initializes a variable total_votes to count the total number of votes cast during the election.

# Define lists and dictionaries to track candidate names and vote counts
list_candidate = []
list_candidate_vote_count = []
## Two empty lists are created: list_candidate to store unique candidate names and list_candidate_vote_count to store dictionaries that track each candidate's name and their respective vote count.

# Winning Candidate and Winning Count Tracker
cand_most_votes = 0
cand_most_name = ''
## This initializes variables to keep track of the candidate with the most votes (cand_most_votes) and the name of that candidate (cand_most_name).

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
## This opens the CSV file specified in file_to_load and creates a CSV reader object to read the file's contents.

# Skip the header row
    header = next(reader)
## This line skips the header row of the CSV file

# Loop through each row of the dataset and process it
    for row in reader:
## This begins a loop that iterates through each row of the CSV data (excluding the header).

# Increment the total vote count for each row
        total_votes += 1
## For each row processed, the total vote count is incremented by one.

# Get the candidate's name from the row
        candidate_name = row[2]
## This extracts the candidate's name from the current row (assuming the candidate's name is in the third column).

# Check if the candidate is already in the candidate list
        if candidate_name not in list_candidate:
            list_candidate.append(candidate_name)
            list_candidate_vote_count.append({'Name': candidate_name, 'Vote Count': 0})
## If the candidate's name is not already in list_candidate, it is added to the list, and a new dictionary is created in list_candidate_vote_count with the candidate's name and an initial vote count of zero.


# Increment the vote count for the candidate
        for candidate in list_candidate_vote_count:
            if candidate['Name'] == candidate_name:
                candidate['Vote Count'] += 1
                break
## This loop checks each candidate in list_candidate_vote_count. When it finds the matching candidate, it increments that candidate's vote count by one.


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
## opens a text file specified in file_to_output for writing the election results.



# Print the total vote count (to terminal)
    print("Election Results")
    print(f"|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|")
    print(f"Total Votes: {total_votes:,}")
    print(f"|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|")
## These lines print the election results header and the total vote count to the terminal, formatting the number with commas.


# Write the total vote count to the text file
    txt_file.write("Election Results\n")
    txt_file.write(f"|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|\n")
    txt_file.write(f"Total Votes: {total_votes:,}\n")
    txt_file.write(f"|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|\n")
## The same information printed to the terminal is also written to the output text file.







#### This is a description of each line of the PyBank main.py code ####

# Dependencies
import csv
import os
## Imports CSV and OS

# get current working directory to make sure the files are present
print(os.getcwd())
## This prints the current working directory 

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "budget_analysis.txt")  # Output file path
## These lines define the file paths for the input CSV file (budget_data.csv) and the output text file (budget_analysis.txt). 

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
total_value = 0
largest_loss = 0
largest_loss_month = "Today"
largest_gain = 0
largest_gain_month = "Today"
average_change = 0
## Variables are set to track various financial metrics, including the total number of months, total net value, total value, largest gain/loss, and average change.


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
## This opens the CSV file and creates a reader object to iterate over the rows in the file.

# Skip the header row
    header = next(reader)
# Extract first row to avoid appending to net_change_list
    print(f"CSV Header: {header}")
## The first line (header) of the CSV is read and stored in the header variable, which is then printed.


# Track the total and net change
    first_data = next(reader)
    total_value = first_data[1]
    total_months = total_months + 1
## The first row of data is read to set total_value and increment total_months by one.

# Process each row of data
    for row in reader:
## loop to process each row of data in the CSV.

# count the months
        total_months = total_months + 1    
## For each row, the total month count is incremented.

# Track the total
        total_value = int(total_value) + int(row[1])
## updates total_value by adding the current row's value.


# Track the net change
        total_net = int(total_net) + int(row[1])
## updates total_net by adding the current row's value, similar to total_value.


# Calculate the greatest increase in profits (month and amount)
        if int(row[1]) > largest_gain:
            largest_gain = int(row[1])
            largest_gain_month = row[0]
## checks if the current row's value is greater than largest_gain. If so, it updates largest_gain and records the corresponding month.

# Calculate the greatest decrease in losses (month and amount)
        if int(row[1]) < largest_loss:
            largest_loss = int(row[1])
            largest_loss_month = row[0]
## checks if the current row's value is less than largest_loss. If so, it updates largest_loss and records the corresponding month.


# Calculate the average net change across the months
# the changes happen over one less month than the total months
average_change = total_net / (total_months - 1)
## calculates the average change by dividing total_net by one less than total_months (since average change is based on changes between months).


# Generate the output summary
 
# Print the output
print(f"Financial Analysis")
## prints the header "Financial Analysis"

print(f"|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|")
## prints a separator line made of dashes and vertical bars, which helps to visually organize the output.

print(f"Total Months: {total_months}")
## prints the total number of months.

print(f"Total Ending Value")
## prints "Total Ending Value" 


# Write the results to a text file
with open(file_to_output, "w") as txt_file:
## opens a file specified variable file_to_output in write mode ("w"). 

#    txt_file.write(output)

txt_file.write(f"Financial Analysis\n")
## writes the header "Financial Analysis" to the text file.
txt_file.write(f"|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|\n")
## writes the same separator line to the text file

txt_file.write(f"Total Months: {total_months}\n")
## writes the total number of months to the text file, followed by a newline character.

txt_file.write(f"Total Ending Value: {"${:,.2f}".format(total_value)}\n")
## writes the total ending value to the text file, formatted as currency with two decimal places. The variable total_value should hold that value.

# txt_file.write(f"Total Change: {"${:,.2f}".format(total_net)}\n")
txt_file.write(f"Average Change: {"${:,.2f}".format(average_change)}\n")
## writes the average change to the text file, formatted as currency with two decimal places.

txt_file.write(f"Greatest Profit (Month / Amount): {largest_gain_month} / {"${:,.2f}".format(largest_gain)}\n")
## writes the month and amount of the greatest profit to the text file, with the amount formatted as currency.

txt_file.write(f"Lowest Profit (Month / Amount): {largest_loss_month} / {"${:,.2f}".format(largest_loss)}\n")
## writes the month and amount of the lowest profit to the text file, with the amount formatted as currency.

