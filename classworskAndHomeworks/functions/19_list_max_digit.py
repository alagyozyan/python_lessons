#!/usr/bin/python3

def get_list_max_digit(ll):
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

def main ():
	l_list = []
	print("Please enter elements of the list.")
	print("To finish entering type 'stop'.")
	while True:
		el = input()
		if el.lower() == 'stop':
			break
		l_list.append(el)

	res = get_list_max_digit(l_list)
	if res == None:
		print ("There is no digital element in the entered list !")
	else: 
		print("The maximum digit element in the entered list is :", res)

main ()

