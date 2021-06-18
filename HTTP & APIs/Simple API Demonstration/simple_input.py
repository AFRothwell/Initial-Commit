# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 20:04:19 2021

@author: Andrew Rothwell
"""

from simple_get_request import GetRequests

user_input = input("Please enter an integer from 1 to 100 (inclusive): ") 

request = GetRequests()

print(request.single_id(user_input).text)