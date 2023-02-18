#!/usr/bin/python3

def to_title (l):
	res = ''
	for el in l:
		code = ord(el[0])
		if (code > 96) and (code < 122) :
			code -= 32
		res += chr(code) + el[1:] + " "
	return res

l = (input ("Please enter some string : ")).split()
result = to_title (l)
print ("All upper case letters converted to lower case : ", result)

