#!/usr/bin/python3

def get_elements_length_list (los):
	if (len(los) == 0):
		return None 
	res = []
	for el in los:
		res.append(len(el))
	return res

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

def print_result(res):
	if res == None:
		print ("There is no any element in the entered list !")
	else: 
		print("Here is the list which elements are the lengths of the entered list elements :", res)

def main ():
	ls = input_list()
	ll = get_elements_length_list(ls)
	print_result (ll)

main ()

