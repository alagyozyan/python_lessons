#!/usr/bin/python3

# Write a Python program that accepts a sequence of comma-separated numbers
# from the user and generates a list and a tuple of those numbers.

temp = input ("Enter some comma-sepereted numbers: ")

print("List :", temp.split(','))
print("Tuple :", tuple(temp.split(',')))
