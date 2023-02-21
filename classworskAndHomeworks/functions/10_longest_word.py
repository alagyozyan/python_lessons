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
	

def main ():
	s = input ("Please enter some string : ")
	l = s.split()
	longest = get_longest_word (l)
	print ("Here is the longest word you entered : ", longest)

main()

