#!/usr/bin/python3

import string

dict = {}

while True:
	mstr = input("enter something: ")
	if mstr.lower() == "stop":
		break
	if mstr.isalpha():
		dict[mstr] = len(mstr)

print(dict)	
