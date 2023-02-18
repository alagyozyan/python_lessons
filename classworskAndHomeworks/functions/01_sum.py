#!/usr/bin/python3

def digits_sum(*l):
    dsum = 0
    for i in l:
        if type(i) == int: 
            dsum += i
    return dsum

print ("The sum of numeric arguments equals :", digits_sum(5, 6, 'ss', 10))

