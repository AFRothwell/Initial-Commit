# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:42:19 2021

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
OOP Exercise 6
-------------------------------------------------------------------------------

Create a Bus child class that inherits from the Vehicle class. The default
fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus
instance, we need to add an extra 10% on full fare as a maintenance charge. So
total fare for bus instance will become the final amount = total fare + 10% of
the total fare.

Note: The bus seating capacity is 50. so the final fare amount should be 5500.
You need to override the fare() method of a Vehicle class in Bus class.

Use the following code for your parent Vehicle class. We need to access the
parent class from inside a method of a child class.
        
-------------------------------------------------------------------------------
'''

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())


