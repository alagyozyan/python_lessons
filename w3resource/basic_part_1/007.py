#!/usr/bin/python3

# Write a Python program that accepts a filename from the user and
# prints the extension of the file. 

file_name = input ("Input the file name : ")
print ("The file extension is :", file_name[(file_name.rindex('.')+1):])

#filename = input("Input the Filename: ")
#f_extns = filename.split(".")
#print ("The extension of the file is : " + repr(f_extns[-1]))