# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 10:26:31 2021

@author: Andrew Rothwell
"""

class LoadFile:
    
    def __init___(self, file_name, file_extension):
        with open(file_name + file_extension) as file:
            text = file.readlines()
    
    
file_name = "poem_input"

file_extension = ".txt"


with open(file_name + file_extension) as file:
    text = file.readlines()