#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 20:18:43 2022

@author: goncalodelacerda
"""

'''
Store all the integers that are multiples of 2 or 5 or 7 that are lower
or equal to 1000
'''
valid_numbers = []
for i in range(1000):
 if (i % 2 == 0) or (i % 5 == 0) or (i % 7 == 0):
     valid_numbers.append(i)

'''
Sum all the integers that are multiples of 2 or 5 or 7 that are lower
or equal to 1000
'''
print(sum(valid_numbers))