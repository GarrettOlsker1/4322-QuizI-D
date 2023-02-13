'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

# open the file

employee_data = open('employee_data.csv', 'w')

# create an empty dictionary

dict = {}

# use a loop to iterate through the csv file

for z in employee_data.csv:
    print(z)

    # check if the employee fits the search criteria
readcsv = csv.reader(employee_data, delimiter(","))

employee_data.write("Name" + "" + "Salary")
print()

for row in readcsv:
    print()

print()
print('=========================================')
print()

# iternate through the dictionary and print out the key and value as per printout

dict = []

dict["First Name"]
dict["Last Name"]
dict["Salary"]


outfile = open("employee_data.csv", "w")
outfile.write("Name, Salary")

list1 = datastore[dict]

for dict in list1:
    Names = dict["Name"]
    New_Sal = dict["Salary"]

outfile.write(str(Names) + ',' + str(New_sal))

outfile.close()
