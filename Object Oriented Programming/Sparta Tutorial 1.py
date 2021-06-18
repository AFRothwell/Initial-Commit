# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 10:34:02 2021

@author: Andrew Rothwell
"""

class Dog:
    
    animal_kind = "canine"   # class_variable
        
    def bark(self):         # method
        return "woof"
    
    
    
print(Dog.animal_kind)
print(Dog().bark())


Myles = Dog()
Oscar = Dog()


    
print(Dog.animal_kind)
print(Dog().bark())

print(type(Myles))
print(type(Oscar))
print(Myles.animal_kind)
print(Oscar.animal_kind)
print(Myles.bark())
print(Oscar.bark())

#Changing one of these two variables won't change the other

Oscar.animal_kind = "Big Dog"

print(Myles.animal_kind)
print(Oscar.animal_kind)
