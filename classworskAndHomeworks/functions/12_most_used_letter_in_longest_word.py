#!/usr/bin/python3

def get_longest_word (wl):
	max_length = 0
	longest_world = ''
	for el in wl:
		l = len(el)
		if l > max_length:
			max_length = l
			longest_world = el
	return longest_world

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
	l = s.split()
	longest = get_longest_word (l)
	letters_dict = get_letters_dict (longest)
	most_used    = get_max_value (letters_dict)
	print ("Here is the longest word you entered :", longest)
	print ("And here is the most used letter in that longest word :", most_used)

main()

