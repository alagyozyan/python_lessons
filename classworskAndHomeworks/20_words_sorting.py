#!/usr/bin/python3

def get_file_content(fn):
	with open(fn) as f:
		return f.read()

def clear_words(word):
	return word.replace(")", "")\
               .replace("(", "")\
               .replace(",", "")\
               .replace("[", "")\
               .replace("]", "")\
               .replace(".", "")\
               .replace(";", "")

def create_words_list(cnt):
	tmp = cnt.split()
	ml = [el.strip("()[]{},.;0987654321") for el in tmp]
	return [el for el in ml if el.isalpha()]

def create_str(word):
	return word + " - " + str(len(word)) + "\n"

def write_into_file(ml, fname):
	with open(fname, "w") as f:
		for el in ml:
			f.write(create_str(el))\

def main():
	fname = "example.txt"
	cnt = get_file_content(fname)
	words = create_words_list(cnt)
	output_file = "result.txt"
	words = list(set(words))
	words.sort()
	write_into_file(words, output_file)

main()
