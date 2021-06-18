# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 09:34:08 2021

@author: Andrew Rothwell
"""

from random import randrange
from sys import exit

class Adventurer:
    
    def __init__(self, name, level = 1, attack = 5, health = 10, mana = 5, coins = 0):
        self.name = name
        self.level = level
        self.attack = attack
        self.health = health
        self.mana = mana
        self.coins = coins
    
class Encounter:
    def __init__(self, location):
        self.location = location
    
    def enemy(self):
    
        encounter_enemy = Enemy(randrange(player.level, player.level + 2, 1))
    
        player_input = input("You encounter a level {} goblin. Will you fight or flee? ".format(encounter_enemy.level))
        
        while player_input != "flee" or "fight":
            if player_input == "fight":
                print("You draw your sword and ready to fight the level {} goblin!".format(encounter_enemy.level))
                
            elif player_input == "flee":
                print("You manage to escape the goblin!")
                
            else:
                print("I'm sorry, I didn't understand your input!")
                player_input = input("You encounter a level {} goblin. Will you fight or flee? ".format(encounter_enemy.level))

class Fight:
    
    def __init__(self, combatants)
        
        self.combatants = combatants
        
    def fight(self):
        print("The goblin is level {}, it has {} health and an attack strength of {}.".format(encounter_enemy(health)))
        
        
class Enemy:
        
    def __init__(self, level = 1, health = 5, attack = 2):
        self.level = level
        self.health = health
        self.attack = attack
    
    
new_game_prompt = input("Would you like to start a new game? y or n? ")

while new_game_prompt != "y" or "n":
    if new_game_prompt == "y":
        player = Adventurer(input("And when tales are told of you, what name shall they sing praise of? "))
        break
    elif new_game_prompt == "n":
        exit(0)
    else:
        print("I'm sorry, I didn't understand your input! Please try again!")
        new_game_prompt = input("Would you like to start a new game? y or n? ")



print("You enter the small village of Upper Fuffner-Figgle, famed for it's prize winning peach cheese. The township have clearly tired of the burden of guiding a seemingly endless queue of keen young adventurers waiting behind a small red rope at the boundary of the village. The nearby yokel posing like a bouncer to a city's most popular nightclub leers at you and ushers you in. They follow a well trodden path inundated with a number of crooked wooden signs accompanying it's full length. The path is met by the foot of a nearby rocky cliff face where a large red panelled door confronts you. You hand off the stub of your 'admit one' ticket and head inside.")

while dead != 1:
    Encounter.enemy("bridge")

