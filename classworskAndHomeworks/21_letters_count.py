#!/usr/bin/python3

def get_file_content(fn):
	with open(fn) as f:
		return f.read()

def get_letter_count(content):
	md = {}
	for el in content:
		if el.isalpha():
			if el in md:
				md[el] += 1
			else:
				md[el] = 1
	return md

def create_str(mt):
	return mt[0] + " - " + str(mt[1]) + "\n"

def write_into_file(ml, fname):
	with open(fname, "w") as f:
		for el in ml:
			f.write(create_str(el))

def main():
	fname = "example.txt"
	cnt = get_file_content(fname)
	letters = get_letter_count(cnt)
	output_file = "result.txt"
	ml = sorted(list(letters.items()), key= lambda x: x[0])
	write_into_file(ml, output_file)

main()
