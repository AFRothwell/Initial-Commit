# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 10:24:17 2021

@author: Andrew Rothwell
"""

class Employee:
    def __init__(self, name, role, age, employeeid = 1):
        self.name = name
        self.role = role
        self.__age = age
        self.__employeeid = employeeid

    def employ(self):
        print(self.__employeeid)

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        print(self.__age)

    def set_employeeid(self, employeeid):
        self.__employeeid += employeeid

    def get_employeeid(self):
        print(self.__employeeid)


Andrew = Employee("Andrew", "CEO", 24, 1)

Andrew.set_age(28)
Andrew.get_age()

Andrew.set_employeeid(1)
Andrew.get_employeeid()
Andrew.set_employeeid(1)
Andrew.get_employeeid()

new_employee = Employee(input("Please enter employee name: "), input("Please enter employee role: "), input("Please enter employee age: "))