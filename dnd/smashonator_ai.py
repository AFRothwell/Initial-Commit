# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 11:49:31 2021

@author: Andrew Rothwell
"""

from random import randint

class Enemy_ai: 
    
    def __init__(self, attack_chance, heal_chance):
        self.attack_chance
        self.heal_chance
        
    def smashonator_ai(self, health):
        
        
        if 30 >= self.health > 20:
            self.attack_chance = range(0,7) #70% attack chance
            self.heal_chance = range(7,10) #30% heal chance
        if 20 >= self.health > 10:
            self.attack_chance = range(0,5) #50% attack chance
            self.heal_chance = range(5,10) #50% heal chance
        if self.health <= 10:
            self.attack_chance = range(0,8) #80% attack chance
            self.heal_chance = range(8,10) #20% heal chance
            
        if randint(0,10) in self.attack_chance:
            return "attack"
        else:
            return "heal"