bags = {}
bagsList = []
normalBoxes = {}
normalBoxesList = []
coldBoxes = {}
coldBoxesList = []
containers = []
customers = {}
customersList = []
shipping = {}
shippingList = []


#The operator has created the containers_to_stored csv file which contains for every container, its ype and dimensions

path = r"C:\Users\Evangelos\Desktop\containers_to_stored.csv"

import pandas as pd 
import csv


df = pd.read_csv(path)


for i, row in df.iterrows():

	#If the container type in the current line of the excel file is Bag
	if (row[0]) == 'Bags':
		#For every row in containers_to_stored csv file, create a dict with keys the container code, type and dimensions
		bags = {'Container code': i, 'Type': row[0], 'Height': row[1], 'Width': row[2], 'Depth': row[3], 'Weight': row[4]}
		#Append each dict to a list of dict
		bagsList.append(bags)

		#Append the list of dict to a list with all the containers that will be used for merging list of dicts later (see line 88)
		containers.append(bags)

	elif (row[0]) == 'Normal Boxes':
		normalBoxes = {'Container code': i, 'Type': row[0], 'Height': row[1], 'Width': row[2], 'Depth': row[3]}
		normalBoxesList.append(normalBoxes)

		#Append the list of dict to a list with all the containers that will be used for merging list of dicts later (see line 88)
		containers.append(normalBoxes)

	elif (row[0]) == 'Cold Boxes':
		coldBoxes = {'Container code': i, 'Type': row[0], 'Height': row[1], 'Width': row[2], 'Depth': row[3]}
		coldBoxesList.append(coldBoxes)

		#Append the list of dict to a list with all the containers that will be used for merging list of dicts later (see line 88)
		containers.append(coldBoxes)



print("\nBags containers stored succesfully\n")
print(bagsList, "\n")
print(len(bagsList), "bags containers are in warehouse\n")

print("\nNormal boxes containers stored succesfully\n")
print(normalBoxesList, "\n")
print(len(normalBoxesList), "normal boxes containers are in warehouse\n")

print("\nCold boxes containers stored succesfully\n")
print(coldBoxesList, "\n")
print(len(coldBoxesList), "cold boxes containers are in warehouse\n")


#The operator has to give the amount of customers for which will be shipped containers
numOfCustomers = int(input("Enter number of customers for shipping: "))


for i in range(0, numOfCustomers):

	#The operator has to give a customer code for every customer
	print("Enter customerCode: ")
	
	customerCode = input()


	#Create a dictionary for every customer 
	customers = {'Customer code' : customerCode}
	#Pass the dicts to a list of dicts with all the customers codes that have been given as input
	customersList.append(customers)


	#Merge the containers list of dicts to the customersList of dicts, so that each container will have a customer code
	for a,b in zip(customersList, containers):
		a.update(b)

#For every customer
for item in customersList:
	#If the assigned to him/her container is bag type
	if item['Type'] == 'Bags':
		#Create a shiiping dict with Bike as value
		shipping = {'Shipping type': "Bike"}
		#Append the dict to a shiiping list of dict 
		shippingList.append(shipping)

	#If the assigned to him/her container is normal boxes or coold boxes type
	elif item['Type'] == 'Normal Boxes' or item['Type'] == 'Cold Boxes':
		#
		shipping = {'Shipping type': "Car"}
		shippingList.append(shipping)



#Merge the customersListofDicts to the Shipping list of dicts with the customersList of dicts, so that each customer will be given the corresponding shipping type (car, or bike)
for c,d in zip(shippingList, customersList):
	c.update(d)

#Pass the headings to variable
field_names= shippingList[0].keys()
 
#new_shipping_fle is a temp file which is created every time the script is called
##The operator has to save the temp file (new_shipping_file) to a permanent file (new_shipping_file_DD:MM:YYY) for every shipping date that the script is called
try:
    with open(" new_shipping_file.csv", 'w',newline='') as csvfile:

    	#Write the headings
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()

        #Write a new line for every new shipping
        for key in shippingList:
            writer.writerow(key)

except IOError:
    print("The temporary file is open. Please, close it to write the new data")