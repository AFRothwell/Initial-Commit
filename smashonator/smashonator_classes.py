# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 11:43:36 2021

@author: Andrew Rothwell
"""

'''
Handles the initialisation and returns the actions taken by the Player and
Enemy AI.

'''

class Player:
    
    def __init__(self, health = 30, attack = 5, heal = 3):
        self.health = health
        self.attack = attack
        self.heal = heal

    def attack(self):
        return self.attack

    def heal(self):
        return self.heal   
    
class Enemy:
 
    def __init__(self, health = 20, attack = 5, heal = 3):
        self.health = health
        self.attack = attack
        self.heal = heal

    def attack(self):
        return self.attack

    def heal(self):
        return self.heal