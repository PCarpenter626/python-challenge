#Importing the Python Libraries 
import os
import csv

total = 0
column_name = 'Profit/Losses'
with open ('budget_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    
#Counting the total months in the File
    total_months = sum(1 for row in reader)

#Counting the total amount of money in the file
with open ('budget_data.csv', 'r') as file:
    reader = csv.DictReader(file)    
    for row in reader:
        total += float(row[column_name])

#Calculating the Average Change
def calculate_average_change(csv_file):
    with open('budget_data.csv', 'r') as file2:
        reader2 = csv.reader(file2)
        next(reader2)  # Dont include the header row in the calculations

        values = []
        for row in reader2:
            values.append(float(row[1])) 

        changes = []
        for i in range(1, len(values)):
            changes.append(values[i] - values[i - 1])

        average_change = sum(changes) / len(changes)
        return average_change

csv_file = 'budget_data.csv'
average_change = calculate_average_change(csv_file)

#Calculating the Greatest Increase 
def calculate_greatest_increase(csv_file):
    with open('budget_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) # Dont include the header row in the calculations 

        max_increase = 0
        max_date = ""
        prev_value = None

        for row in reader:
            date1 = row[0]
            value = float(row[1])

            if prev_value is not None:
                increase = value - prev_value
                if increase > max_increase:
                    max_increase = increase
                    max_date = date1

            prev_value = value

    return max_date, max_increase

csv_file = "budget_data.csv"  
date1, increase = calculate_greatest_increase(csv_file)

#Calculating the Greatest Decrease 
def calculate_greatest_decrease(csv_file):
    with open('budget_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Dont include the header row in the calculations 

        greatest_decrease = 0
        min_date = ""
        previous_value = None
        
        for row in reader:
            try:
                date2 = row[0]
                value = float(row[1])  
            except (ValueError, IndexError):
                continue

            if previous_value is not None:
                change = value - previous_value
                if change < greatest_decrease:
                    greatest_decrease = change
                    min_date = date2
            previous_value = value

    return min_date, greatest_decrease

csv_file_path = 'budget_data.csv'
date2, decrease = calculate_greatest_decrease(csv_file_path)
min_date = date2

#Outputting the Code to a Textfile
with open('PyBank_Output.txt', "w") as textfile: # a is for append, r is for reading
            textfile.write(
    
                f"Financial Analysis \n" 
                f" -------------------- \n"
                f" Total Months: {total_months} \n"
                f" Total:  $   {total} \n" 
                f" Average change: $ {round(average_change,2)}\n" 
                f" Greatest Increase in Profits: {date1} ($ {increase}) \n"
                f" Greatest Decrease in Profits: {date2} ($ {decrease}) \n"
    )
#Code to Output to a Terminal
print("Financial Analysis")
print("-" *20) 
print("Total Month:" , " " , total_months)
print("Total: " " " "$", total)
print("Average change:" " " "$" ,round(average_change,2))
print("Greatest Increase in Profits: " , date1, " " "$", increase)
print("Greatest Decrease in Profits: " , date2, " " "$", decrease)