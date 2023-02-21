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

def create_ilist_of_tuples (l):
	if (len(l) == 0):
		return None
	lot = []
	for el in l:
		lot.append((len(el), el))
	return lot

def get_sorted_list (tl):
	if tl  == None:
		return None
	temp = sorted(tl, key=lambda s: s[0], reverse=True)
	r = []
	for el in temp:
		r.append(el[1])
	return r

def print_result(res):
	if res == None:
		print ("There is no element in the entered list !")
	else: 
		print("Here is thei list of descednding ordered elements :", res)

def main ():
	el_list  = input_list()
	tuple_list = create_ilist_of_tuples (el_list)
	res = get_sorted_list(tuple_list)
	print_result (res)

main ()

