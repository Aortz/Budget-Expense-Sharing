import pandas as pd

no_of_pax = 6
total_amount = 138
paid_py_person = [47,37,24,0,30,0]
namelist = ["Pek","Shilin","Junwei","Matt","Clement","Chin Wei"]

#creating fuction to calculate the difference in amount paid by specific person and average amount per pax
def per_pax_payment(paid_py_person, no_of_pax, total_amount):
	averageAmount = paymentcalc(no_of_pax, total_amount)
	amount_owed_by_thisguy = averageAmount - paid_py_person
	return (round(amount_owed_by_thisguy, 2))

#function to calculate average cost of the bill
def paymentcalc(no_of_pax, total_amount):
	amount_to_pay_per_pax = total_amount/no_of_pax
	return(round(amount_to_pay_per_pax, 2))

#function to calculate difference between those owing money and those who needs to be paid
def getDiff(x,y):
	difference = x + y
	return difference

#Payment by person in a list form in descending order


#Creating a drop down option, where user inputs amounts paid in descending order
#Creation of input values to replace hard coded elements in namelist, for user interface


#create dictionary for difference in amount that everyone paid
my_dict = {}
def makeDict(namelist, paid_py_person):
	count = 0
	while count < no_of_pax:
		my_dict[namelist[count - 0]] = per_pax_payment(paid_py_person[count], no_of_pax, total_amount)
		count += 1
	return my_dict

makeDict(namelist, paid_py_person)

#split dictionary into those who paid and those who didn't
#create two list with amounts outstanding and amounts due
dict_for_ppl_owing_money = {}
dict_for_ppl_owed_money = {}
total_amount_oustanding = [] #creating a counter to keep track of total sum outstanding after deductions

for name, value in my_dict.items(): #sorting keys and values into those who paid and those who didnt
	if value < 0:
		dict_for_ppl_owed_money[name] = float(value)
		namelist_of_those_owed_money = list(dict_for_ppl_owed_money.keys())
		amount_owed = list(dict_for_ppl_owed_money.values())

	else:
		dict_for_ppl_owing_money[name] = float(value)
		amount_of_those_owing_money = list(dict_for_ppl_owing_money.values())
		namelist_of_those_owing_money = list(dict_for_ppl_owing_money.keys())


for values in amount_owed:
	total_amount_oustanding.append(values * -1)

total_amount_oustanding = sum(total_amount_oustanding)

payment_dict = {}

#creating an algorithm to determine distribution of funds
#compare the difference in amount first person havent paid and first person paid

payor = 0 #initialise value to first element in the dictionaries
difference = 0 #initialising first value of difference

while total_amount_oustanding > 0: #creating a sentinel value to stop the programme when outstanding <0

	try:
		name_for_currentperson_owing_money = namelist_of_those_owing_money[0]
		#defining key for name in dict for those who owe money against first name in those that didn't 
		whotowho = f"{name_for_currentperson_owing_money} owes {namelist_of_those_owed_money[payor]}" 
	except IndexError: #error handling for the case where they delete the first element in the dictionary and list when there is nothing left to compare to
		break
	finally:
		pass
	
	actual_difference = round(getDiff(amount_owed[payor], amount_of_those_owing_money[payor]), 2)

	if actual_difference > 0: #aka those owing money paid amount > the first person who's owed money
		#value is negative so *-1 to make it a positive amount and amount owed is the entire sum of the first person paid money
		payment_dict[whotowho] = amount_owed[payor] * -1
		total_amount_oustanding += amount_owed[payor] #updating counter
		#after deduction is done, update the dictionary to remove the first person paid
		amount_of_those_owing_money[payor] = actual_difference
		dict_for_ppl_owing_money[name_for_currentperson_owing_money] = actual_difference
		del amount_owed[payor]
		del dict_for_ppl_owed_money[namelist_of_those_owed_money[payor]]
		del namelist_of_those_owed_money[payor]

	elif actual_difference <= 0:
		payment_dict[whotowho] = amount_of_those_owing_money[payor]
		total_amount_oustanding -= amount_of_those_owing_money[payor]
		del dict_for_ppl_owing_money[name_for_currentperson_owing_money]
		dict_for_ppl_owed_money[namelist_of_those_owed_money[payor]] = actual_difference
		amount_owed[payor] = actual_difference
		del amount_of_those_owing_money[payor]
		del namelist_of_those_owing_money[payor]

print(payment_dict)
