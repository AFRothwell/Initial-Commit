# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 16:17:30 2021

@author: Andrew Rothwell
"""

class PlayerStats:
    
    def __init__(self, subclass, level = 1, strength, dexterity, wisdom):
        self.subclass = subclass
        self.level = level
        self.strength = strength
        self.dexterity = dexterity
        self.wisdom = wisdom        
        
        
class Fighter(PlayerStats):
    
    def __init__(self, subclass = "Fighter", strength = 3, dexterity = 2, wisdom = 1):
        self.subclass = subclass
        self.strength = strength
        self.dexterity = dexterity
        self.wisdom = wisdom

class Ranger(PlayerStats):
    
    def __init__(self, subclass = "Fighter", strength = 1, dexterity = 3, wisdom = 2):
        self.subclass = subclass
        self.strength = strength
        self.dexterity = dexterity
        self.wisdom = wisdom
        
class Wizard(PlayerStats):
    
    def __init__(self, subclass = "Wizard", strength = 1, dexterity = 2, wisdom = 3):
        self.subclass = subclass
        self.strength = strength
        self.dexterity = dexterity
        self.wisdom = wisdom