# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 10:34:02 2021

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
OOP Exercise 2
-------------------------------------------------------------------------------

    Create a class "Vehicle"
        without either:
            - Variables     (e.g. x = 1)
            - Methods       (see Notes below)

-------------------------------------------------------------------------------
Notes
-------------------------------------------------------------------------------

Methods:

-   A method in python is somewhat similar to a function, except it is
    associated with object/classes.

-   Methods in python are very similar to functions except
    for two major differences:

    1. The method is implicitly used for an object for which it is called.

    2. The method is accessible to data that is contained within the class.

  - Example:
        
    class Pet(object):
        def my_method(self):
            print("I am a Cat")
    cat = Pet()
    cat.my_method()

  - Example Output:
    
    I am a Cat

-------------------------------------------------------------------------------
'''

class Vehicle:
    pass