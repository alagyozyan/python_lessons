#!/usr/bin/python3

def get_two_digits_elements (ll):
	rl = []
	for el in ll:
		if el.isdigit() and (len(el) == 2) and (int(el) % 2 == 0):
			rl.append(el)
	if len(rl) == 0:
		return None
	else:
		return rl
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
		print ("There is no two digit even element in the entered list !")
	else: 
		print("Here are the two digits even elements of the entered list :", res)

def main ():
	l = input_list()
	r = get_two_digits_elements(l)
	print_result (r)

main ()

