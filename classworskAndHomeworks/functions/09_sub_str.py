#!/usr/bin/python3

def get_substr (s, b, e):
	return s[b:e]

def main ():
	s = input ("Please enter some string : ")
	while True:
		start = input ("Please enter start position : ")
		if start.isdigit():
			start = int(start)
			break
		else:
			print ("Please enter integer value !")
	while True:
		end = input ("Please enter end position : ")
		if end.isdigit():
			end = int(end)
			break
		else:
			print ("Please enter integer value !")

	sstr = get_substr (s, start, end)
	print ("Here is the substring from given borders : ", sstr)

main()

