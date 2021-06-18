# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:38:33 2021

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
OOP Exercise 5
-------------------------------------------------------------------------------

Define a class attribute ”color” with a default value white.

I.e., Every Vehicle should be white.
        
-------------------------------------------------------------------------------
Notes
-------------------------------------------------------------------------------

Variables created in .__init__() are called instance variables.
An instance variable’s value is specific to a particular instance of the
class. For example, in the solution, All Vehicle objects have a name and a
max_speed, but the name and max_speed variables’ values will vary depending on
the Vehicle instance.


On the other hand, class attributes are attributes that have the same value
for all class instances. You can define a class attribute by assigning a value
to a variable name outside of .__init__().

-------------------------------------------------------------------------------
'''

class Vehicle:
    # Class attribute
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)