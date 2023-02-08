#!/usr/bin/python3

num = int(input("Enter a integer number: "))

if num % 15 == 0:
	print("The entered number is FizzBuzz!")
elif num % 5 == 0:
	print("The number is Buzz!")
elif num % 3 == 0:
	print("The number is Fizz!")
else:
	print("The number is not Fizz or Buzz!")
	
