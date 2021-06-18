# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 11:11:20 2021

@author: Andrew Rothwell
"""


class Dog:
    
    animal_kind = "canine"
    
    def __init__(self, name, colour):
        self.animal_kind = "canine"
        self.name = name
        self.colour = colour
        self.bark()
        
    def bark(self):
        print("woof")
    

Myles = Dog("Myles", "Golden")

print(Myles.name)
print(Myles.colour)