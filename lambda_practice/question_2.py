# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:40:28 2021

@author: Andrew Rothwell
"""

'''
Write a Python program to create a function that takes one argument, and that
argument will be multiplied with an unknown given number.
'''


def func1(arg1):
    return lambda λ : λ * arg1
'''
Calling the function with lambda in it allows us to define a variable that
will take an argument for the value of lambda later
'''

# arg 1 = 2
result = func1(2)

# λ = 15
print(result(15))