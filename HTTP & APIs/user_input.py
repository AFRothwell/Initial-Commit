# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 09:56:46 2021

@author: Andrew Rothwell
"""

from get_requests import GetRequests

get = GetRequests()


# Prints all posts from a specific UserId

user_input = input("Please enter a number from 1 to 10: ")

while user_input not in range(1,11):
    
    try:
        user_input = int(user_input)
    except ValueError:
        user_input = input("Please enter a number from 1 to 10: ")  


print(get.single_user_id(user_input).text)




user_input = input("Please enter an integer from 1 to 100: ")

while user_input not in range(1,101):
    
    try:
        user_input = int(user_input)
    except ValueError:
        user_input = input("Please enter an integer from 1 to 100: ")

print(get.single_id(user_input).text)