#!/usr/bin/python3

def isPolyndrom(s):
	if s == s[::-1]:
		return True
	return False 

sstr = input("Enter some string: ")
if isPolyndrom(sstr):
	print("The string You entered is polindorm")
else:
	print("The string You entered is not polindrom")



