#This is the Source Code of Part B.2 Password Security Strength Evaluator App by : Rawan Amr Abdelsattar

# importing the library used to get all alphabet letters
import string

# intializing our characters list in each type 
lowercase_alphabet = list(string.ascii_lowercase)
uppercase_alphabet = list(string.ascii_uppercase)
symbols = ["@", "?","=", "<",">",":","{", "}","!", "#", "%", "$", "*", "&", "^", "~", "'", ";", "/", "-", "_", "(", ")"]
numbers = [0,1,2,3,4,5,6,7,8,9]


# the running of our application depends on this variable , it's true until the user types in 'q'
run = True

# app's loop
while run :

	# prompting user to type in a password
	print("\nThis is the password security strength evaluator app")
	password = input("\nType in your password or type 'q' to quit: ").replace(" ", "")
	
	# checking if the user wants to quit
	if password == "q":
		run = False

	else:

		# simple function to return check sign or wrong based on condition 
		def checkOrNot(cond):
			return "(√)" if cond else "(X)"

		# checking password contents and length against conditions/rules
		contains_number_and_symbol = checkOrNot(any(str(i) in password for i in numbers) and any(i in password for i in symbols))
		contains_lower_and_upper_case = checkOrNot(any(i in password for i in uppercase_alphabet) and any(i in password for i in lowercase_alphabet))
		is_12_or_more_charcters = checkOrNot(len(password) >= 12)
		valid = "Valid" if contains_number_and_symbol == "(√)" == "(√)" and contains_lower_and_upper_case == "(√)" and is_12_or_more_charcters == "(√)" else "Invalid"
		

		# displaying the check results to the user
		print("""Conditions:
			1.length is 12 or more characters {}
			2.contains uppercase and lowercase letters {}
			3.contains a number a symbol {}
			
			{} Password  !
			""".format(is_12_or_more_charcters, contains_lower_and_upper_case, contains_number_and_symbol, valid))

	

