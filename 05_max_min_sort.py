#!/usr/bin/python3

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

mmax = num1
mmin = num1

if (num2 > mmax):
	mmax = num2
if (num3 > mmax):
	mmax = num3

if (num2 < mmin):
	mmin = num2
if (num3 < mmin):
	mmin = num3

print("\nMaximum number is", mmax)
print("Minimum number is", mmin)
print("Here are the list of sorted numbers:", mmin, (num1 + num2 + num3 - (mmax + mmin)), mmax)
