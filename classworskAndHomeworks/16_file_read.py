#!/usr/bin/python3
	
def return_file_content():
	return open("example.txt").read()

def longest_word(f_content):
	word_list = f_content.split()
	max_length = 0
	for el in word_list:
		length = len(el)
		if length > max_length:
			max_length = length
			longest_word = el
	return longest_word

def return_used_letters_count(f_content):
	chars = {}
	for letter in f_content:
		if letter.isalpha():
			if letter in chars.keys():
				chars[letter] += 1	
			else:
				chars.update({letter: 0})
	return chars

def return_reversed_content(f_content):
	r_content = ""
	for letter in f_content:
		r_content = letter + r_content
	return r_content

def return_reversed_words(f_content):
	rw_content = ""
	word_list = f_content.split()
	for word in word_list:
		r_word = ""
		for letter in word:
			r_word = letter + r_word
		rw_content = rw_content + " " + r_word
	return rw_content

def return_sentence_count(f_content):
	s_list =f_content.split(".")
	for i in s_list:
		print (i)
	return len(s_list)
	
file_content = return_file_content()
print (longest_word(file_content))
print (return_used_letters_count(file_content))
print (return_reversed_content(file_content))
print (return_reversed_words(file_content))
print ("There are %d sentences in the file." % return_sentence_count(file_content))
