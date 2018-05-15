#! Python2
#passStrength.py - Checks if a given password is considered strong.
#Strong passwords are at least 8 chars long, has both upper and lower case and has at least 1 digit.

import re


def passwordCheck(password):
	#check for pass length
	if len(password) < 8:
		print 'Your password is too short.'
		lengthCheck = False

	else:
		lengthCheck = True

	#check for lower case
	lowerCheckRegex = re.compile(r'[a-z]+')
	if lowerCheckRegex.search(password) == None:
		print 'Your password has no lower case characters.'
		lowerCheck = False

	else:
		lowerCheck = True

	#check for upper case
	upperCheckRegex = re.compile(r'[A-Z]+')
	if upperCheckRegex.search(password) == None:
		print 'Your password has no upper case characters.'
		upperCheck = False

	else:
		upperCheck = True
	#check for numbers
	numCheckRegex = re.compile(r'[0-9]+')
	if numCheckRegex.search(password) == None:
		print 'Your password has no numbers in it.'
		numCheck = False

	else:
		numCheck = True


	if lengthCheck == lowerCheck == upperCheck == numCheck == True:
		print 'Your password is strong! Good job!'
		return False

	else:
		print 'Your password is weak, consider using a different password and trying again.'
		return True

password = ""
checking = True
while checking == True:
	password = raw_input("Please enter the password to check it's strength: ")
	checking = passwordCheck(password)
