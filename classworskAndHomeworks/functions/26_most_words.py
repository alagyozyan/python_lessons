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


def print_result(res):
	if res == None:
		print ("There is no element in the entered list !")
	elif res == '':
		print ("There is no words in the entered list.")
	else: 
		print("Here is the string which contains the most of words :", res)

def get_most_words (l):
	if len(l) == 0:
		return None
	max_c = 0
	max_s = ''
	for el in l:
		wc = len(el.split())
		if wc > max_c:
			max_c = wc
			max_s = el
	return max_s

def main ():
	el_list  = input_list()
	res = get_most_words(el_list)
	print_result (res)

main ()

