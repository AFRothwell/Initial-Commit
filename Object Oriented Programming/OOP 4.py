# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 11:27:42 2021

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
OOP Exercise 4
-------------------------------------------------------------------------------

Create a Bus class that inherits from the Vehicle class.

Give the capacity argument of Bus.seating_capacity() a default value of 50.

Use the following code for your parent Vehicle class.

You need to use method overriding.
        
-------------------------------------------------------------------------------
'''

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())