#!/usr/bin/python3

def get_sub_polindrom(mstr, length):
    for i  in range(len(mstr)-1):
        s = mstr[i:length]
        
        if s == s[::-1]:
            print("Found polindrom :", s)
        length = length + 1

get_sub_polindrom("soosovwpefvbvbqarraiejrnvn", 3)

