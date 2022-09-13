one_a = [0,1,2,3,4,5,6,7,8,9]
three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}

three_a = three_setE.issubset(three_setA)	#checking if set E is subset of A 

three_b = three_setE.issuperset(three_setA)	#checking if E is a superset of A

three_c = three_setA.intersection(three_setB)	#checking intersecting elements of A and B

three_d = three_setC.union(three_setD, three_setE)	#check union of set C, D and E

three_e = three_d.add(9)	#adding 9 to set D. Since set won't allow repetition, we cannot see 9 getting added to the set

#three_f
if three_d == one_a: 	#comparing set to list 
	print (True)
else:
	print(False)

#three_g
# They are not the same since list one_a and set three_d are not the same type. 
# To make them equal, we have to convert set to list or vice versa.  
