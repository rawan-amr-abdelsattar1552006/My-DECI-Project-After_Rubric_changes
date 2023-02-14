# This is the Source Code of Part B.3 Data Confidentiality App by : Rawan Amr Abdelsattar

# importing the library used to get all alphabet letters
import string

# intializing our characters list in each type 
lowercase_alphabet = list(string.ascii_lowercase)
uppercase_alphabet = list(string.ascii_uppercase)
numbers = ["0","1","2","3","4","5","6","7","8","9"]


# function used to shift the characters based on 4 params
def shift(char, key, list, mode):
	# shifting characters to the right to encrypt them
	if mode == "encryption":
		if list.index(char) + key > len(list) - 1:
			index = (list.index(char) - len(list)) + key
			while index > len(list) - 1:
				index -= len(list)
		else :
			index = list.index(char) + key

	# shifting characters to the left to decrypt them
	elif mode == "decryption":
		if list.index(char) - key < 0:
			index = (list.index(char) - key) + len(list) 
			while index < 0:
				index += len(list)
		else :
			index = list.index(char) - key
	
	shifted_char = list[index]
	return shifted_char


AppEnd = False

#App's loop
while not AppEnd:
	# Prompting the user to choose a service 
	service = input("\nType 'e' for encryption mode or 'd' for decryption mode or 'q' to quit: \n(e/d/q): ")
	
	# Checking if user wanted to quit the application
	if service == 'q':
		AppEnd = True

	# Checking if user selected the encryption serivce
	elif service == 'e' :
		plain_text = input("\nType the plain text to be encrypted: ")
		cipher_text = ""

		# prompting the user to input a key
		key_input = input("\n\nType a key (only numbers are accepted): ")

		# boolean to control the key validation loop
		invalid = True

		# validating the key to check if it's an integer
		while invalid:
			if not key_input.isdigit():
				print("\nInvalid key, only integers are allowed..")
				key_input = input("\n\nType a key (only numbers are accepted): ")
			else:
				invalid = False
				key = int(key_input)

		# shifting characters based on their type
		for char in plain_text:
			if char in numbers:
				cipher_text += shift(char, key, numbers, "encryption")
			elif char in lowercase_alphabet:
				cipher_text += shift(char, key, lowercase_alphabet, "encryption")
			elif char in uppercase_alphabet:
				cipher_text += shift(char, key, uppercase_alphabet, "encryption")
			else:
				cipher_text += char

		# displaying the result to the user
		print("\n\nEncryption Done !\nCipher-text is : " + cipher_text)				

	# Checking if user selected the decryption serivce
	elif service == 'd':
		cipher_text = input("\n\nType the cipher text to be decrypted: ")
		plain_text = ""

		key_input = input("\n\nType a key (only numbers are accepted): ")

		# boolean to control the key validation loop
		invalid = True

		# validating the key to check if it's an integer
		while invalid:
			if not key_input.isdigit():
				print("\nInvalid key, only integers are allowed..")
				key_input = input("\n\nType a key (only numbers are accepted): ")
			else:
				invalid = False
				key = int(key_input)

		# shifting characters based on their type
		for char in cipher_text:
			if char in numbers:
				plain_text += shift(char, key, numbers, "decryption")
			elif char in lowercase_alphabet:
				plain_text += shift(char, key, lowercase_alphabet, "decryption")
			elif char in uppercase_alphabet:
				plain_text += shift(char, key, uppercase_alphabet, "decryption")
			else:
				plain_text += char

		# displaying the result to the user
		print("\n\nDecryption Done !\nPlain-text is : " + plain_text)				


	

	# checking if user input is an invalid service, and re-prompting input
	else:
		print("\n\nInvalid Service, Please try again..")
		service = input("\n\nType 'e' for encryption service or 'd' for decryption service : \n(e/d/q): ")
