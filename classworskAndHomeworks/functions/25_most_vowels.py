#!/usr/bin/python3

def input_list ():
	l_list = []
	print("Please enter elements of the list.")
	print("To finish entering type 'stop'.")
	while True:
		el = input()
		if el.lower() == 'stop':
			break
		l_list.append(el)
	return l_list

def get_most_vowels_word (l):
	if l == None:
		return None
	vowels = ['a', 'e', 'i', 'o', 'u']
	max_v = 0
	result = ''
	for el in l:
		count = 0
		for l in el:
			if l in vowels: 
				count += 1
		if count > max_v:
			max_v = count
			result = el
	return result

def print_result(res):
	if res == None:
		print ("There is no element in the entered list !")
	elif res == '':
		print ("There is no word which contains any vowel.")
	else: 
		print("Here is the string which contains the most of vowels :", res)

def main ():
	el_list  = input_list()
	w = get_most_vowels_word (el_list)
	print_result (w)

main ()

