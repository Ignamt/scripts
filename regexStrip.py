#! python2
#regexStrip.py - Este script es para una funcion con Regexes que agarre una string y le borre de
#las puntas los caracteres que le paso. Default es whitespace.

import re

def regexStrip(string, char_to_strip='\s'):
	#check if string is a stringType.
	while type(string) != type("string"):
		print 'You must pass a string to the function.'

	#create the regex with char_to_strip
	stripRegex = re.compile(r'^%s*(\S+(\s\S+)*)%s*$' %(char_to_strip, char_to_strip))

	strip = stripRegex.search(string)
	return strip.group(1)

newString = regexStrip("    Hi! How are you doing?    ")
print newString

