def per_pax_payment(paid_py_person, no_of_pax, total_amount):
	averageAmount = paymentcalc(no_of_pax, total_amount)
	amount_owed_by_thisguy = averageAmount - paid_py_person
	return (round(amount_owed_by_thisguy, 2))


def paymentcalc(no_of_pax, total_amount):
	amount_to_pay_per_pax = total_amount/no_of_pax
	return(round(amount_to_pay_per_pax, 2))

def getDiff(x,y):
	if x < y:
		difference = x + y
	elif y < x:
		difference = y
	return difference

#Payment by person in a list form in descending order

no_of_pax = 3
total_amount = 270.00
paid_py_person = [97, 82, 91]

#Creating a drop down option, where user inputs amounts paid in descending order
#Creation of input values to replace hard coded elements in namelist, for user interface
namelist = ["Justin", "Junwei", "Adrian"]

#create dictionary for amount everyone paid
my_dict = {}
def makeDict(namelist, paid_py_person):
	count = 1
	while count < no_of_pax + 1:
		my_dict[namelist[count - 1]] = per_pax_payment(paid_py_person[count - 1], no_of_pax, total_amount)
		count += 1
	return my_dict

makeDict(namelist, paid_py_person)

#split dictionary into those who paid and those who didn't
#create two list with amounts outstanding and amounts due
dict_for_ppl_owing_money = {}
dict_for_ppl_owed_money = {}
total_amount_oustanding = []

for name, value in my_dict.items():
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

#creating an algorithm to determine distribution of funds
#compare the difference in amount first person havent paid and first person paid

payor = 0
difference = 0

while total_amount_oustanding > 0:
	name_for_currentperson_owing_money = namelist_of_those_owing_money[payor]
	try:
		whotowho = str(name_for_currentperson_owing_money) + " owes " + str(namelist_of_those_owed_money[payor])
	except IndexError:
		break
	finally:
		pass
	
	difference = round(getDiff(amount_owed[payor], amount_of_those_owing_money[payor]), 2)

	if difference > 0:
		dict_for_ppl_owing_money[whotowho] = amount_owed[payor] * -1
		total_amount_oustanding += amount_owed[payor]
		del amount_owed[payor]
		del dict_for_ppl_owed_money[namelist_of_those_owed_money[payor]]
		del namelist_of_those_owed_money[payor]

	elif difference <= 0:
		dict_for_ppl_owing_money[whotowho] = amount_of_those_owing_money[payor]
		total_amount_oustanding -= amount_of_those_owing_money[payor]
		del dict_for_ppl_owing_money[name_for_currentperson_owing_money]
		dict_for_ppl_owed_money[namelist_of_those_owed_money[payor]] = difference
		amount_owed[payor] = difference
		del amount_of_those_owing_money[payor]
		del namelist_of_those_owing_money[payor]

print(dict_for_ppl_owing_money)

#creation of error handling method in case of mismatched between total amount inputted and total amount paid by individual users
#error handling for when number of elements in a namelist doesn't match number of elements for amounts paid


# for name, payee in dict_for_ppl_owed_money.items():
# 	#creating new key in outstanding dict for who paid who
# 	name_for_currentperson_owing_money = list(dict_for_ppl_owing_money.keys())[payor]
# 	whotowho = str(name_for_currentperson_owing_money) + " owes " + str(namelist_of_those_owed_money[payor])
# 	difference = round(getDiff(amount_owed[payor], amount_of_those_owing_money[payor]), 2)

# 	if difference > 0:
# 		dict_for_ppl_owing_money[whotowho] = amount_owed[payor] * -1
# 		del amount_owed[payor]
# 		# del dict_for_ppl_owed_money[namelist_of_those_owed_money[payor]]
# 		del namelist_of_those_owed_money[payor]
# 		amount_of_those_owing_money[payor] = difference
# 		whotowho = str(name_for_currentperson_owing_money) + " owes " + str(name)
# 		difference = round(getDiff(amount_owed[payor], amount_of_those_owing_money[payor]), 2)
# 		dict_for_ppl_owing_money[whotowho] = amount_of_those_owing_money[payor] - difference

# 		# difference = round(getDiff(amount_owed[payor], amount_of_those_owing_money[payor]), 2)
# 		# if difference > 0:
# 		# 	dict_for_ppl_owing_money[whotowho] = amount_of_those_owing_money[payor] - difference
# 		# else:
# 		# 	continue

# 		# del dict_for_ppl_owed_money[name_for_currentperson_owing_money]
# 		# del namelist_of_those_owing_money[payor]




# 	elif difference <= 0:
# 		dict_for_ppl_owing_money[whotowho] = amount_of_those_owing_money[payor]
# 		del dict_for_ppl_owing_money[name_for_currentperson_owing_money]
# 		dict_for_ppl_owed_money[name] = difference
# 		del amount_of_those_owing_money[payor]
# 		amount_owed[payor] = difference

# print(dict_for_ppl_owing_money)


