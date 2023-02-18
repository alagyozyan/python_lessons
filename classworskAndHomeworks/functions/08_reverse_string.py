#!/usr/bin/python3

def str_reverse (s):
	return s[::-1]

s = input ("Please enter some string : ")
reversed_result = str_reverse (s)
print ("Here is the reversed string you entered : ", reversed_result)

