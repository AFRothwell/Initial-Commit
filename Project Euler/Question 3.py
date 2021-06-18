# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 14:14:56 2021

@author: Andrew Rothwell
"""

'''

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

prime factor = prime number AND factor.

'''

import math

largestprime = 0

bignumber = 600851475143

sqrtbig = math.floor(math.sqrt(600851475143))


for number in range(2,sqrtbig):
    divisor = number - 1
    
    if bignumber % number == 0:
        while (number % divisor != 0) and (number > 0):
            divisor -= 1
        
        if divisor == 1:
            largestprime = number
            print(largestprime)
            
            
'''

The square root of a number denotes the point on the number line at which the
factor pairs of that number are

'''