# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 11:43:28 2021

@author: Andrew Rothwell
"""

'''
Turn based combat against a single AI controlled opponent.

Main Topic:
- Object Oriented Programming

'''



from smashonator_classes import Player
from smashonator_classes import Enemy
from smashonator_ai import Enemy_ai

player = Player()
enemy = Enemy()
turn = 0
print("Fight for your life against the Great Smashonator!")


while player.health and enemy.health > 0:

    if turn == 0:
        player_input = input("Would you like to attack or heal? ")
        if player_input == "attack":
            enemy.health -= Player.attack(player)
            print("You attack the Great Smashonator for {} HP! They have {} health left!".format(Player.attack(player),max(0, enemy.health)))
            turn = 1
            continue
        elif player_input == "heal":
            player.health += Player.heal(player)
            print("You heal for {} HP! You have {} health left!".format(Player.heal(player), player.health))
            turn = 1
        else:
            print("I'm sorry, I didn't understand your input! Please try again!")
            continue
    
    if turn == 1:
        ai_input = Enemy_ai.smashonator_ai(enemy, enemy.health)
        if ai_input == "attack":
            player.health -= Enemy.attack(enemy)
            print("The Great Smashonator smashes you for {} HP! You have {} health left!".format(Enemy.attack(enemy), max(0, player.health)))
            if player.health <= 0:
                print("You have been defeated by the Great Smashonator!!!")
                break
            else:
                turn = 0
        elif ai_input == "heal":
            enemy.health += Enemy.heal(enemy)
            print("The Great Smashonator heals for {} HP! They have {} health left!".format(Enemy.heal(enemy), enemy.health))
            turn = 0

if player.health <= 0:
    print("You have been defeated by the Great Smashonator!!!")
    
elif enemy.health <= 0:
    print("You have defeated the Great Smashonator!!!")