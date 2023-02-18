#!/usr/bin/python3

def arithmetic_operations (n, m):
	aol = []
	aol.append(n + m)
	aol.append(n - m)
	aol.append(n * m)
	aol.append(n / m)
	aol.append(n % m)
	return aol

num1 = float (input("Please enter the first digit : "))
num2 = float (input("Please enter the second digit : "))

res = arithmetic_operations(num1, num2)

print ("{} + {} = {}\n".format(num1, num2, res[0]))
print ("{} - {} = {}\n".format(num1, num2, res[1]))
print ("{} * {} = {}\n".format(num1, num2, res[2]))
print ("{} / {} = {}\n".format(num1, num2, res[3]))
print ("{} % {} = {}\n".format(num1, num2, res[4]))

