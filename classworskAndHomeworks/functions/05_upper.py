#!/usr/bin/python3

def to_upper (s):
	res = ''
	for el in s:
		code = ord(el)
		if (code > 96) and (code < 122) :
			code -= 32
		res += chr(code)
	return res

st = input ("Please enter some string : ")
result = to_upper(st)
print ("All lower case letters converted to upper case : ", result)

