#This is the Source Code of Part B.1 Secure Password Generator App by : Rawan Amr Abdelsattar
# I read the docs of the "random" and "tkinter" libraries from 'https://www.geeksforgeeks.org/'

# Importing the library used to make random choices
import random

# Importing the library used to make the GUI
import tkinter as myTk

# Importing the library to get the alphabet in both upper and lower case
import string


# Intializing the window variable and customizing it
window = myTk.Tk()
window.title("Secure Password Generator")
window.resizable(False, False)



# Intializing alphabet, numbers, and symblos list to be easily used
lowercase_alphabet = list(string.ascii_lowercase)
uppercase_alphabet = list(string.ascii_uppercase)
symbols = ["@", "!", "#", "%", "$", "*", "&", "^", "~", "'", ";", "/", "-", "_", "(", ")"]
numbers = [0,1,2,3,4,5,6,7,8,9]






def btnClick():
	# Resetting my variables
	password_characters = []
	password = ""
	
	# Deleting what was in the Text widget
	mytxt.delete("1.0","end")
	for i in range(0,3):
		password_characters.append(random.choice(lowercase_alphabet))
		password_characters.append(random.choice(uppercase_alphabet))
		password_characters.append(random.choice(symbols))
		password_characters.append(random.choice(numbers))

	# Shuffling the list to make it more secure and at an upredictible arrangement of character types
	random.shuffle(password_characters)

	# Putting the characters together into one string to be easily displayed 
	for i in range(0,len(password_characters)):
		password += str(password_characters[i])
	mytxt.insert(myTk.END,"Your Secure Password is : " + password+"\n\nHighlight it and press Ctrl+c to copy it\n\nThe conditions/rule are that any generated password must :\n1.be at least 12-character long\n2.contain Uppercase and Lowercase letters\n3.contain at least one special character or symbol (ex. @, $, #, etc. )\n4.contain numbers" )


# setting up the widgets for the GUI
mytxt = myTk.Text(window, width = 60, height=13)

mytxt.insert(myTk.END,"Click on the button to generate your password")
mytxt.pack()
myBtn = myTk.Button(window, text="Generate Password",width=40, command=btnClick)
myBtn.pack()

window.mainloop()