#!/usr/bin/python3

def order_by_name_length (l):
	return sorted(l, key=lambda s: len(s['name']), reverse=True)

def main ():
	u1 = {'name':'Harvard University',						'location':'US'}
	u2 = {'name':'University of Cambridge',					'location':'UK'}
	u3 = {'name':'Stanford University',						'location':'US'}
	u4 = {'name':'University of Oxford',					'location':'UK'}
	u5 = {'name':'Massachusetts Institute of Technology', 	'location':'US'}
	u6 = {'name':'California Institute of Technology',		'location':'US'}
	u7 = {'name':'Imperial College London',					'location':'UK'}

	ul = [u1, u2, u3, u4, u5, u6, u7]		# Universities list
	obnl = order_by_name_length(ul)			

	print ("Here is the university which name is the longest : '{}'".format(obnl[0]['name']))

main ()

