#!/usr/bin/python3

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

mmax = num1

if (num2 > mmax):
	mmax = num2
if (num3 > mmax):
	mmax = num3

if (mmax > (num1 + num2 + num3 - mmax)):
	print("It's not possible to creat triangle !")
else:
	p = (num1 + num2 + num3) / 2
	s = pow(p*(p-num1)*(p-num2)*(p-num3), 1 / 2)
	print("The square of our triangle is:", s )
