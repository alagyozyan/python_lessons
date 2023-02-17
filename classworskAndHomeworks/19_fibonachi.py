#!/usr/bin/python3
fd = {1:1, 2:1}
i = 1
# Recursive function with linear difficulty
def LRFibonacci (num):
	global i
	if num == 1: 
		return 
	fd.update({i+2:(fd[i] + fd[i+1])})
	i += 1	
	LRFibonacci(num-1)

# Recursive function with exponential difficulty
def RFibonacci (num):
	if num == 1 or num == 2:
		return 1
	return RFibonacci(num-1) + RFibonacci(num-2)


def Fibonacci (num):
	l = [1, 1]
	i = 0
	while i < num:
		l.append(l[i] + l[i+1])
		i += 1
	return l[num-1]

n = int(input("Please enter an integer : "))

print ("Result of simple function using 'while' loop.")    
print ("In the sequence of Fibonacci, the element number {} is : {}\n".format(n, Fibonacci(n))) 

print ("Result of recursive function with exponential difficulty : ")
print ("In the sequence of Fibonacci, the element number {} is : {}\n".format(n, RFibonacci(n))) 

LRFibonacci(n)
print ("Result of recursive function with linear difficulty : ")
print ("In the sequence of Fibonacci, the element number {} is : {}\n".format(n, fd[n])) 
