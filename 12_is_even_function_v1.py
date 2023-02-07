#!/usr/bin/python3


def isEven(num):

	if num % 2 == 0:
		return True
	return False

num = int(input("Enter a non-zero number: "))
print (isEven(num))
