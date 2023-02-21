#!/usr/bin/python3

def get_letters_dict (s):
	ld = {}
	for l in s:
		if l.isalpha():
			l = l.lower()
			if l in ld.keys():
				ld[l] += 1
			else:
				ld[l] = 1
	return ld

def get_max_value (ld):
	max_v = 0
	result_key = '' 
	for el in ld.keys():
		if ld[el] > max_v:
			max_v = ld[el]
			result_key = el
	return {result_key:max_v}
	
def main ():
	s = input ("Please enter some string : ")
	letters_dict = get_letters_dict (s)
	most_used    = get_max_value (letters_dict)
	print ("Here is the most used letter in your entered text : ", most_used)

main()

