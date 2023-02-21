#!/usr/bin/python3

def get_str_count (ll):
	s_count = 0
	for el in ll:
		if el.isalpha():	
			s_count += 1
	return s_count


def main ():
	l_list = []
	print("Please enter elements of the list.")
	print("To finish entering type 'stop'.")
	while True:
		el = input()
		if el.lower() == 'stop':
			break
		l_list.append(el)

	print("Number of strings in the entered list is :", get_str_count(l_list))

main ()

