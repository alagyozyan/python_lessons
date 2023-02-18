#!/usr/bin/python3


def string_count(*l):
    count = 0
    for i in l:
        if type(i) == str: 
            count += 1
    return count

print ("The total number of string arguments is :", string_count(5, 'bcd', 'ased', 6, 'ss', 10))

