# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 15:11:55 2021

@author: Andrew Rothwell
"""

'''

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''


results = [[],[],[]]

for n1 in range(999,99,-1):
    palindrome = 0

    n2 = 999
    
    while n2 > 99 and palindrome == 0:
       
        result = (n1 * n2)
        result = str(result)
        if result[::-1] == result:
            palindrome = 1
            results[0].append(int(result))
            results[1].append(n1)
            results[2].append(n2)
        
        n2 -= 1
        
max_value = max(results[0])

max_index = results[0].index(max_value)

number_1 = results[1][max_index]
number_2 = results[2][max_index]
largest_palindrome = results[0][max_index]

print("The largest palindrome made from the product of two 3-digit numbers is {}, it is created from the product of {} and {}.".format(largest_palindrome,number_1,number_2))