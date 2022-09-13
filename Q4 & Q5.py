three_setA = {1,2,3,4,5}
################################################# QUESTION 4 ######################################################

four_a = int(8)

four_b = []			#Creating an empty list 

four_c = four_b.append(type(four_a))  #Appending type of four_a to empty list 

four_d = four_b.append(0.39)	#Appending 0.39 to list 

four_e = four_b.append(type(0.39))	#Appening type of 0.39 to the list 

exponential = round(0.39 ** -10) 	#using a variable to carry out exponential process and wounding it up 

four_f = four_b.append(exponential)	#Appending the integer of exponential to empty list

four_g = four_b.append(type(exponential))	#Appending the type of exponential to empty list 


################################################# QUESTION 5 ######################################################

five_a = {"int" : 0.39, "float" : 12284}		#Creating a dictionary manually, based on list from four_b

five_b1 = four_b.append(300)	#Appending 300 to the empty list 

five_b = str(300)	#converting the int to string

five_c = four_b.append(type(five_b))	#pppending the type of string to list four_b

five_d = five_b[:2]			#slicing the string till second element 

five_e = four_b.append(type(five_d))	#appneding the type of five_d to the list 

five_f = [int(s) for s in five_b.split() if s.isdigit()]	#creating a new list using list comprehension which contains only integers

five_g = four_b.append(type(five_f))	#appending type of five_f to list from question 4

five_h = four_b.append(type(three_setA))	#appending type of three_SetA to the list from question 4
