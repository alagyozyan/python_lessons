#!/usr/bin/python3

def order_by_points (l):
	return sorted(l, key=lambda s: s['points'])

def main ():
	s1 = {'name':'Armen',   'age':25, 'points':256}
	s2 = {'name':'Karen',   'age':30, 'points':485}
	s3 = {'name':'Ashot',   'age':22, 'points':754}
	s4 = {'name':'Varduhi', 'age':18, 'points':421}
	s5 = {'name':'Stepan',  'age':24, 'points':125}
	s6 = {'name':'Mher',    'age':21, 'points':251}
	s7 = {'name':'Minas',   'age':26, 'points':326}
	s8 = {'name':'Mariam',  'age':18, 'points':726}

	sl = [s1, s2, s3, s4, s5, s6, s7, s8]		# Students list
	ol = order_by_points(sl)					# Oldest student

	for el in ol:
		print ("{}\t\t{}\t\t{}".format(el['name'], el['age'], el['points']))

main ()

