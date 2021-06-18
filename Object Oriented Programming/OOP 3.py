# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 11:20:35 2021

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
OOP Exercise 3
-------------------------------------------------------------------------------

    Create a child class "Bus" that will inherit all of the following from the
    parent class "Vehicle":
        
        - Variables
        - Methods
        
-------------------------------------------------------------------------------
'''

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Bus(Vehicle):
    pass
    
School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)