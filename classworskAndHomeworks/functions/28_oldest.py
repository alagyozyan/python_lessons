#!/usr/bin/python3

def get_oldest_student (l):
	oldest = 0
	oldest_student = {}
	for el in l:
		if el['age'] > oldest:
			oldest = el['age']
			oldest_student = el
	return oldest_student

def main ():
	s1 = {'name':'Armen',   'age':25}
	s2 = {'name':'Karen',   'age':30}
	s3 = {'name':'Ashot',   'age':22}
	s4 = {'name':'Varduhi', 'age':18}
	s5 = {'name':'Stepan',  'age':24}
	s6 = {'name':'Mher',    'age':21}

	sl = [s1, s2, s3, s4, s5, s6]		# Students list
	os = get_oldest_student(sl)				# Oldest student

	print ("The oldest student is {}, who is {} years old.".format(os['name'], os['age']))

main ()

