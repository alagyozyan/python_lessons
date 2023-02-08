#!/usr/bin/python3

# Write a Python program that accepts an integer (n) and
# computes the value of n+nn+nnn.

snum = input ("Input some integer : ")
res = int(snum) + int(2*snum) + int(3*snum)
print ("Expected result is :", res)  

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)