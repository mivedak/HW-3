# File: main.py
import os
import csv

# create a variable to store the months
Total_Months = 0
Profit = 0
change = 0
temp = 0
dates = []
avg_chg = []



# create a variable to store the file path of csv file
csv_file = os.path.join("Resources","budget_data.csv")

#open the file in read mode
with open(csv_file, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # Reading the header row
    header_row = next(csv_reader)
    
   #Reading the first row (so that we track the changes properly)
    first_row = next(csv_reader)
    Total_Months = Total_Months + 1
    Profit += int(first_row[1])
    temp = int(first_row[1])


# loop through all rows
    for row in csv_reader:

    # keeping track of dates
        dates.append(row[0])
    
    #add the months to Total Months
        Total_Months = Total_Months + 1
    
    # Find total number of profit
        Profit += int(row[1])

    # Find average of change
        # creat a temp list to store the difference between 2 numbers
        change = int(row[1]) - temp
        avg_chg.append(change)
        temp = int(row[1])

        
# calculating the greatest increase in profit
greatest_increase = max(avg_chg)
greatest_index = avg_chg.index(greatest_increase)
greatest_date = dates[greatest_index]

# calculating the greatest decrease in profit
greatest_decrease = min(avg_chg)
lowest_index = avg_chg.index(greatest_decrease)
lowest_date = dates[lowest_index]
        
#calculate the average of change from the list on line number 40
Average_Profit_Change = sum(avg_chg) / len(avg_chg)

#Displaying information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(Total_Months)}")
print(f"Total: ${str(Profit)}")
print(f"Average Change: ${str(round(Average_Profit_Change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {lowest_date} (${str(greatest_decrease)})")


## Writing to a text file ##

# Store output filepath in a variable
output_file = open("output.txt", "w")

output_file.write("Financial Analysis\n")
output_file.write("---------------------\n")
output_file.write(f"Total Months: {str(Total_Months)}\n")
output_file.write(f"Total: ${str(Profit)}\n")
output_file.write(f"Average Change: ${str(round(Average_Profit_Change,2))}\n")
output_file.write(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})\n")
output_file.write(f"Greatest Decrease in Profits: {lowest_date} (${str(greatest_decrease)})\n")

