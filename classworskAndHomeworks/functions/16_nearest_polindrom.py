#!/usr/bin/python3

def isPolyndrom(s):
	if s == s[::-1]:
		return True
	return False 

def get_nearest_polindrom(num):
	slength = len(num)
	smiddle = slength // 2
	if slength % 2 == 0:
		return num[:smiddle] + num[(smiddle-1)::-1]
	else:
		return num[:(smiddle+1)] + num[(smiddle-1)::-1]

def main():
	while True:
		i = input ("Please enter some integer: ")
		if i.isdigit():
			break
		else:
			print ("Please enter an integer !")

	msg = "The nearest polindrom is :"
	if isPolyndrom(i):
		print(msg, i)
	else:
		print(msg, get_nearest_polindrom(i))
	
main ()
