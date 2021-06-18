# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 16:04:17 2021

@author: Andrew Rothwell
"""


class Car:
    
    def __init__(self, max_speed, mileage, model):
        self.max_speed = max_speed      # max speed (mph)
        self.mileage = mileage          # miles per gallon (mpg)
        self.type = model            # car type being driven
        self.fuel_tank_size = 12        # max fuel tank size (gallons)
        self.fuel_level = 0             # the current fuel level (gallons)
        
        
    # Sets the current fuel_level to fuel_tank_size.
    def fuel_up(self):
        self.fuel_level = self.fuel_tank_size   
        print("Fuel tank is now full.")
        
    def refuel(self, new_level):
        print("Fuel is current £5 a gallon.")
        
        refuel_input = input("How many gallons would you like to input? ")
        
        while self.fuel_tank_size < refuel_input:
            print("Capacity Exceeded!")
                refuel_input = input("How many gallons would you like to input? ")
        
        if (fuel_tank_size - fuel_tank
        
        if new_level <= self.fuel_tank_size - self.fuel_level: 
        self.fuel_level += new_level    
        
        
Ford = Car(120, 40, "Fiesta")


Car.fuel_up(Ford)

