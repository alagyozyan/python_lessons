#!/usr/bin/python3

def input_list ():
	msg = "Please enter some sentence which contains any numbers."
	return (input(msg).split())

def get_max_number (ll):
	max_el = 0
	flag = False
	for el in ll:
		if el.isdigit():
			d = int(el)
			if d > max_el:	
				max_el = d
				flag = True
	if flag:
		return max_el
	else:
		return None

def print_result (r):
	if r == None:
		print ("There is no digital element in the entered sentence !")
	else: 
		print("The maximum number in the entered sentence is :", r)
	return

def main ():
	el_list  = input_list()
	res = get_max_number(el_list)
	print_result (res)

main ()

