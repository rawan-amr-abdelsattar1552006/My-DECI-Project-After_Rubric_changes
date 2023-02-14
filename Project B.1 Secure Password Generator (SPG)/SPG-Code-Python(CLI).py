#This is the Source Code of Part B.1 Secure Password Generator App by : Rawan Amr Abdelsattar
# I read the docs of the "random" library from 'https://www.geeksforgeeks.org/python-random-module/'

# Importing the library used to make random choices
import random

#Importing the library to get the alphabet in both upper and lower case
import string

lowercase_alphabet = list(string.ascii_lowercase)
uppercase_alphabet = list(string.ascii_uppercase)
symbols = ["@", "!", "#", "%", "$", "*", "&", "^", "~", "'", ";", "/", "-", "_", "(", ")"]
numbers = [0,1,2,3,4,5,6,7,8,9]

run = True

# App's loop
while run :

	# Prompting the user to choose to generate a password or to quit 
	choice = input("\nType 'g' to generate a secure password or 'q' to quit\n(g/q): ")
	password_characters = []
	password = ""

	# checking if the user wants to quit
	if choice == 'q':
		run = False

	# random and secure password generation process
	elif choice == 'g':
		for i in range(0,3):
			password_characters.append(random.choice(lowercase_alphabet))
			password_characters.append(random.choice(uppercase_alphabet))
			password_characters.append(random.choice(symbols))
			password_characters.append(random.choice(numbers))

		# shuffling the password characters list to make it more secure and at an unpredictable pattern
		random.shuffle(password_characters)

		# putting all the characters of the password_characters list in one string
		for i in range(0,len(password_characters)):
			password += str(password_characters[i])

		# displaying the output
		print("Your Secure Password is : " + password+  "\n\nHighlight it and press Ctrl+c to copy it\n\nThe conditions/rule are that any generated password must :\n1.be at least 12-character long\n2.contain Uppercase and Lowercase letters\n3.contain at least one special character or symbol (ex. @, $, #, etc. )\n4.contain numbers" ) 

	# prompting user to input a valid choice
	else:
		print("Invalid input , try again...")
		choice = input("\nType 'g' to generate a secure password or 'q' to quit\n(g/q): ")
