# This is the Source Code of Part B.4 Data Integrity App by : Rawan Amr Abdelsattar

# Importing the library used to implement the md5 hashin algorithm
import hashlib
import os

# Setting up some variables
run = True
myHash = ""

# App loop
while run :
	validating = True 

	# Prompting the user to select their desired service 
	print("\nPress 'c' for integrity check or 'q' to quit")
	service = input("(c/q): ")
	
	# Checking if the user wants to quit
	if service == "q":
		run = False

	# Checking if the user wants to check file's integrity
	elif service == "c":
		file_path = input("Type in the path to the file you want to check: ").replace("\\", "/").replace('"', "")
		hash_input = input("Type in the file's pre-calculated hash : ").replace("\\", "/").replace('"', "").strip()
		
		# opening the file and the corresponding hash file (checking if the input is valid)
		while validating:
			if os.path.isfile(file_path):
				file = open(file_path , "r")
				validating = False
			else:
				print("Please Enter a valid path: ")
				file_path = input("Type in the path to the file you want to check: ").replace("\\", "/").replace('"', "")
	
		

		# Reading the file into string
		file_data = file.read()
		
		
		# Generating our own md5 hash of the file
		myHash = hashlib.md5(file_data.encode()).hexdigest()
		
		# checking if the input/pre-calculated hash matches with the generated/calculated hash
		if myHash == hash_input:
			print("\nThe calculated hash is: " + myHash)
			print("\nIntegrity Confirmed, the two hashes match!")
		else:
			print("\nThe calculated hash is: " + myHash)
			print("\nIntegrity Violated, the two hashes don't match")


		file.close()