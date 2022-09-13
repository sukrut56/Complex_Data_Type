one_a = [0,1,2,3,4,5,6,7,8,9]

one_b = one_a.insert(5,3)			#Adding 3 to 5th index position 

one_c = [float(i) for i in one_a]	#Using for loop to coerce list to float

one_d= set(one_a)					#converting list to a set using .set() function 

one_e = one_d.add(10)

one_f = one_d.remove(5)

one_g = len(one_d)			# number of elements in set

number_of_elements_in_list = len(one_c)	#number of elements in the list


if number_of_elements_in_list == one_g:			#comparing the number of elements in set and list are same or not 
	print('Same number of elements')			#If they contain same number of elements, then prints same number of elements
else: 
	print('Different number of lements')		#if they contain different number of elements, then prints different number of elements

set_to_list = list(one_d) 			#converting set to list 

one_i = one_a + set_to_list 		#using '+' operator to combine list and list 

one_j = set(one_i)					#converting list from one_i to set 

one_k = len(one_j)					#counting the length of elements in one_j
