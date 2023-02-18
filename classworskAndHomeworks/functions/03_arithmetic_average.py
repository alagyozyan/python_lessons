#!/usr/bin/python3

def  arithmetic_average(*l):
	aa = 0
	c = 0
	for i in l:
		aa += i
		c  += 1
	return ( aa / c )

print ("The arithmetic average equals : ", arithmetic_average(5, 10, 20, 10))
	
