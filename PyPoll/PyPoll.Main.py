#Importing the Python Libraries 
import os
import csv 

with open ('election_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    
#counting the total votes from the file
    total_votes = sum(1 for row in reader)

#counting the number of times CCS appears in the data
def count_occurrences1(csv_file, column_name, value_to_count1):
    
    count1 = 0
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row[column_name] == value_to_count1:
                count1 += 1
    return count1

csv_file = 'election_data.csv'  
column_name = 'Candidate'  
value_to_count1 = 'Charles Casper Stockham'  

occurrences1 = count_occurrences1(csv_file, column_name, value_to_count1)

#counting the number of times DD appears in the data
def count_occurrences2(csv_file, column_name, value_to_count2):
    
    count2 = 0
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row[column_name] == value_to_count2:
                count2 += 1
    return count2

csv_file = 'election_data.csv'  
column_name = 'Candidate'  
value_to_count2 = 'Diana DeGette' 

occurrences2 = count_occurrences2(csv_file, column_name, value_to_count2)

#counting the number of times RAD appears in the data
def count_occurrences3(csv_file, column_name, value_to_count3):
    
    count3 = 0
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row[column_name] == value_to_count3:
                count3 += 1
    return count3

csv_file = 'election_data.csv'  
column_name = 'Candidate'  
value_to_count3 = 'Raymon Anthony Doane'  

occurrences3 = count_occurrences3(csv_file, column_name, value_to_count3)

#Calculating the Percentages of the votes from each candidate
Percent1 = f"{occurrences1 / total_votes  * 100:.3f}%" 
Percent2 = f"{occurrences2 / total_votes  * 100:.3f}%" 
Percent3 = f"{occurrences3 / total_votes  * 100:.3f}%" 

#Outputting the Code to a Textfile
with open('PyPoll_Output.txt', "w") as textfile: 
            textfile.write(
            f" Election Results \n"
            f" - - - - - - - - - - - \n"
            f" Total Votes: {total_votes} \n" 
            f" - - - - - - - - - - - \n"  
            f" {value_to_count1} : {Percent1} ({occurrences1}) \n"
            f" {value_to_count2} : {Percent2} ({occurrences2}) \n"
            f" {value_to_count3} : {Percent3} ({occurrences3}) \n"
            f" - - - - - - - - - - - \n"
            f" Winner: {value_to_count2} \n" 
            f" - - - - - - - - - - -"
    )
#Code to Output to a Terminal (MAC)
print("Election Results") 
print("-" *20) 
print("Total Votes:" " ", total_votes )
print("-" *20) 
print(value_to_count1, " " , Percent1,  occurrences1) 
print(value_to_count2, " " , Percent2,  occurrences2) 
print(value_to_count3, " " , Percent3,  occurrences3) 
print("-" *20) 
#Calculating the Winner based on the votes
if occurrences1 > occurrences2 and  occurrences1 > occurrences3:
    print("Winner is Charles Casper Stockham ")
elif occurrences2 > occurrences1 and occurrences2 > occurrences3:
    print("Winner is Diana DeGette")
elif occurrences3 > occurrences1 and occurrences3 > occurrences2:
   print("Winner is Raymon Anthony Doane")
print("-" *20) 