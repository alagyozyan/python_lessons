#!/usr/bin/python3

def Fibonacci (num):
	l = [1, 1]
	i = 0
	while i < num:
		l.append(l[i] + l[i+1])
		i += 1
	return l[num-1]

def RFibonacci (num):
	if num == 1 or num == 2:
		return 1
	return RFibonacci(num-1) + RFibonacci(num-2)

print (Fibonacci(int(input("Please enter an integer : "))))    
print (RFibonacci(int(input("Please enter an integer : "))))    
