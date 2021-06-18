# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 16:39:04 2021

@author: Andrew Rothwell
"""

class Car:
    
    def __init__(self, max_speed, mileage, model):
        self.max_speed = max_speed      # max speed (mph)
        self.mileage = mileage          # miles per gallon (mpg)
        self.type = model               # car type being driven
        self.fuel_tank_size = 12        # max fuel tank size (gallons)
        self.fuel_level = 8             # the current fuel level (gallons)
        
        
    # Sets the current fuel_level to fuel_tank_size.
    def fuel_up(self):
        self.fuel_level = self.fuel_tank_size   
        print("Fuel tank is now full.")
        
    def refuel(self):
        print("Fuel is currently £5 a gallon.")
        
        refuel_input = int(input("How many gallons would you like to input? "))
        
        while (self.fuel_tank_size - self.fuel_level) < refuel_input:
            print("Capacity Exceeded!")
            return refuel_input
        
        else:
            print(f"{refuel_input} gallons at a going rate of £5 per gallon is going to cost £{5*refuel_input}")
            refuel_confirmation = input("Do you wish to add this amount? Enter 'y' or 'n' to confirm. ")
            
            if refuel_confirmation == "y":
                self.fuel_level += refuel_input
                print("Ok, you have successfully refuelled")
                
            elif refuel_confirmation == "n":
                print("Refuelling cancelled, you have not been charged with this transaction.")
                refuel_exit = input("Would you like to continue refuelling? Enter 'y' or 'n' to confirm. ")
            else:
                print("I'm sorry I did not understand your command.")
                print(f"{refuel_input} gallons at a going rate of £5 per gallon is going to cost £{5*new_level}")





def refuel(self):
    print("Fuel is currently £5 a gallon.")
    new_level = int(input("How many gallons would you like to refuel? "))
    while self.fuel_tank_size - self.fuel_level <= new_level:
        print("Exceeded capacity")
        new_level = int(input("How many gallons would you like to refuel? "))
    else:
        self.fuel_level += new_level
        print(f"This is going to cost £{5*new_level}")
        
             
Ford = Car(120, 40, "Fiesta")


Car.refuel(Ford)