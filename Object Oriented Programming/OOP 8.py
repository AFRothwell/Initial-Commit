# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:46:11 2021

@author: Andrew Rothwell
"""

'''
-------------------------------------------------------------------------------
Python Object-Oriented Programming (OOP)
    Exercise: Classes and Objects Exercises
-------------------------------------------------------------------------------

Source: https://pynative.com/python-object-oriented-programming-oop-exercise/

Python Object-oriented programming (OOP) is based on the concept of “objects,”
which can contain data and code:
    
    Data in the form of instance variables
    (often known as attributes or properties).
    
    Code in the form method: I.e., Using OOP, we encapsulate related
    properties and behaviors into individual objects.



This OOP exercise covers questions on the following topics:

- Class and Object creation
- Instance variables and Methods, and Class level attributes
- Model systems with class inheritance i.e., inherit From Other Classes
- Parent Classes and Child Classes
- Extend the functionality of Parent Classes using Child class
- Object checking

References

- https://pynative.com/python-object-oriented-programming/   

- https://pynative.com/python-inheritance/

-------------------------------------------------------------------------------
OOP Exercise 8
-------------------------------------------------------------------------------

Determine if School_bus is also an instance of the Vehicle class.
        
-------------------------------------------------------------------------------
'''

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

# use Python's built-in isinstance() function
print(isinstance(School_bus, Vehicle))