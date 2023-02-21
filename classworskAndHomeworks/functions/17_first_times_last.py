#!/usr/bin/python3

def get_firs_times_last (num):
	return int(num[0]) * int(num[-1])

def main ():
	while True:
		i = input ("Please enter some integer: ")
		if i.isdigit():
			break
		else:
			print ("Please enter an integer !")
	print("The first digit times the last digit of the entered number equals to :", get_firs_times_last(i))
	
main ()
