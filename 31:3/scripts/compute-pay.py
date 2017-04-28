# -*- coding: utf-8 -*-
"""
@filename: computepay.py
@author: cyruslentin
"""

h = input("Enter Hours: ")

r = input("Enter Rate: ")

if float(h) <= 40:
	pay = float(h) * float(r)
else:
	pay = (40 * float(r)) + ( (float(h)-40) * (float(r)*1.5) )

print(pay)
