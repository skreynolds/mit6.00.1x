#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 16:50:02 2017

@author: shane

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
For problems such as these, do not include raw_input statements or define the variable s in any way. Our automated testing will provide a value of s for you - so the code you submit in the following box should assume s is already defined. If you are confused by this instruction, please review L4 Problems 10 and 11 before you begin this problem set.
"""

s = 'azcbobobegghakl'

"""My code here"""

count = 0;

for i in range(0,len(s)-2):
    if s[i:i+3] == 'bob':
        count += 1;
        
print('Number of bob: ' + str(count))