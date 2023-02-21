#!/usr/bin/python3
def get_sub_str (s, b, e):
	if b == 0:
		return s[:e]
	if e == 0:
		return s[:b:-1]
	
def main ():
	s = input ("Please enter some string : ")
	l = len(s)
	while True:
		i = input ("Please enter index : ")
		if i.isdigit():
			i = int(i)
			if i > l:
				print ("please enter less than -", l)
				continue
			break
		else:
			print ("Please enter integer value !")

	sstr_1 = get_sub_str (s, 0, i)
	sstr_2 = get_sub_str (s, i, 0)

	print ("Here is substring from beginning :", sstr_1)
	print ("Here is substring from the end :", sstr_2)

main()
