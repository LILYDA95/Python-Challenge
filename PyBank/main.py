#Start by importing
import os
import csv

#Set path
csvpath = "/Users/lilyda/Python-Challenge/PyBank/Resources/budget_data.csv"

#Create a list to store the data
budget_data = []

#Define Variables
total_months = []
change_profit_losses = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0


#Open CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skip the header labels to iterate with the values
    header = next(csvreader)  

    #Read through the rows in the stored file contents
    for row in csvreader: 
        
        #Count of months
        count_months += 1

        #Net total amount of "Profit/Losses" over the entire period
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months == 1):
            #Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            # Compute change in profit loss 
            change_profit_loss = current_month_profit_loss - previous_month_profit_loss

            # Append each month to the months[]
            total_months.append(row[0])

            # Append each change_profit_losses to the change_profit_losses[]
            change_profit_losses.append(change_profit_loss)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss

    #sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(change_profit_losses)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    # highest and lowest changes in "Profit/Losses" over the entire period
    highest_change = max(change_profit_losses)
    lowest_change = min(change_profit_losses)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    highest_month_index = change_profit_losses.index(highest_change)
    lowest_month_index = change_profit_losses.index(lowest_change)

    # Assign best and worst month
    best_month = total_months[highest_month_index]
    worst_month = total_months[lowest_month_index]

# -->>  Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")

