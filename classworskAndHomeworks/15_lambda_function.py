#!/usr/bin/python3

mstr = input ()
ml = mstr.split()
#nl = [el for el in ml if len(el) > 4]
fl = list(filter (lambda  x : len(x) > 4, ml))
kl=list(map(lambda  x : len(x) > 4, ml))
print (fl)
print (kl)
