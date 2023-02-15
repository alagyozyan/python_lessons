#!/usr/bin/python3

def Factorial (num):
	if num == 0:
		return 1
	f = 1
	while num != 1:
		f *= num
		num -= 1
	return f

number = input ("please enter some integer number : ")
print ("The Factioral of %s number equals to %d:" % (number, Factorial(int(number))))

