# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 11:43:36 2021

@author: Andrew Rothwell
"""

from random import randint

class Player:
    
    def __init__(self, health = 30, gold_looted = 1, melee_damage = range(2,4), quiver_size = 3, hit_chance = 50, thrown_damage = 25, mana_pool = 5, trap_evasion = 25, magic_damage = range(2,5)):
        self.health = health
        self.gold_looted = gold.looted
        self.melee_damage = melee_damage
        self.quiver_size = quiver_size
        self.hit_chance = hit_chance
        self.thrown_damage = thrown_damage
        self.mana_pool = mana_pool
        self.trap_evasion = trap_evasion
        self.magic_damage = magic_damage

    def melee_attack(self, melee_damage, hit_chance):
        if hit_chance >= randint(0, 100):
            return 1
        else:
            return 0
    
    def thrown_attack(self, thrown_damage, hit_chance):
        if hit_chance >= randint(0,100):
            return 1
        else:
            return 0
    
    def magic_attack(self, mana_pool):
        return 1
    
    def heal(self):
        return 1
    
class Enemy:
 
    def __init__(self, health = 20, attack = 5, heal = 3):
        self.health = health
        self.attack = attack
        self.heal = heal

    def attack(self):
        return self.attack

    def heal(self):
        return self.heal