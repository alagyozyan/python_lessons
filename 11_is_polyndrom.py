#!/usr/bin/python3

def isPolyndrom(s):
	if s == s[::-1]:
		return True
	return False 

sstr = input("Enter some string: ")
print(isPolyndrom(sstr))



