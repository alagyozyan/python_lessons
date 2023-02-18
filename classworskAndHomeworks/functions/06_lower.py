#!/usr/bin/python3

def to_lower (s):
	res = ''
	for el in s:
		code = ord(el)
		if (code > 64) and (code < 91) :
			code += 32
		res += chr(code)
	return res

st = input ("Please enter some string : ")
result = to_lower (st)
print ("All upper case letters converted to lower case : ", result)

