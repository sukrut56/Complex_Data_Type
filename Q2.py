two_patient_dictionary_kinoko = {"name" : "Kinoko", "year" : 2021}
two_patient_dictionary_dango = {"name" : "Dango", "year" : 2019}
two_patient_dictionary_mochi  = {"name" : "Mochi", "year" : 2020}


two_a = {"two_patient_dictionary_kinoko" : two_patient_dictionary_kinoko, "two_patient_dictionary_dango" : two_patient_dictionary_dango, "two_patient_dictionary_mochi" : two_patient_dictionary_mochi }	#combining three sample dictionaries

two_b = (two_a['two_patient_dictionary_dango']['name'])		#Using keys method to retrive Dango's name 

two_a['two_patient_dictionary_mochi'] = {"name" : "Mochi", "year" : 2018}	#Updating the value of Machi using keys

two_d = {"kinoko" : 2021, "dango" : 2019, "mochi" : 2019}		#creating a dictionary manually

two_e = list(two_d.keys())		#Converting keys of two_d into list 

two_f = list(two_d.values())	#Converting values of two_d into list 

two_g = dict(zip(two_e, two_f))	#zippping the two lists to dictionary b