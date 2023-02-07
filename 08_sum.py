#!/usr/bin/python3

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

if (num1 % 2 != 0):
	num1 += 1

for i in range(num1, num2, 2):
	print(i)
