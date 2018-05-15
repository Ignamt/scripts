#!usr/bin/python2
#Phone and Email Extractor	
#This script will take the info on the clip board and extract only the phone numbers and e-mails
from __future__ import unicode_literals
import pyperclip, re

#Find all phone numbers 
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?				#area code
	(\s|-|\.)?						#separator
	(\d{3})							#first 3 digits
	(\s|-|\.)?						#separator
	(\d{4})							#Last 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?	#Extension
	)''', re.VERBOSE)

#Email regex 
emailRegex = re.compile(r'''(
	[a-zA-Z0-9%._+-]+		#username
	@
	[a-zA-Z0-9.-]+			#domain name
	(\.[a-zA-Z]{2,4})		#dot something
	(\.[a-zA-Z]{2,4})?		#second dot something
	)''', re.VERBOSE)

#Find matches in regex text. El mail lo queres como aparece, pero el telefono lo queremos
#agregar en un formato standard, por eso se lo arma de esa forma
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	phoneNum = "-".join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])


#TODO: Copy results to the clipboard
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print 'Copied to clipboard:'
	print '\n'.join(matches)

else:
	print 'No phone or email matches were found.'
