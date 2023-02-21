#!/usr/bin/python3

def get_digital_elements (ll):
	rl = []
	for el in ll:
		if el.isdigit():
			rl.append(int(el))
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
		print ("There is no digital element in the entered list !")
	else: 
		print("Here are the digital elements arthmetic avearge of the entered list :", res)

def get_arithmetic_average(digits):
	if digits == None:
		return None
	return sum(digits)/len(digits)
		
def main ():
	l = input_list()
	d = get_digital_elements(l)
	a = get_arithmetic_average(d)
	print_result (a)

main ()

