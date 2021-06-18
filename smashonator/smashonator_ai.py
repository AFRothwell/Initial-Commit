# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 11:49:31 2021

@author: Andrew Rothwell
"""

'''

A basic AI I created to handle the enemy for the smashonator project

I originally implemented a simple "coin toss" 50/50 chance for the enemy to
heal or attack the player. After completing the project on time, I went back
and made the necessary changes to implement a more advanced AI.

I've found a lot of interest in how challenge can offer it's own reward to a
player. In my experience, an opponent that remains elusive and difficult to
predict offers a large increase in the value of attempting to defeat them.

See the original stalkers in Tom Clancy's the Division. Originally a hidden
and incredible challenge that would unpredictably engage the player at any
time, their purpose has now unfortunately been relegated to overblown loot
goblins with annoying abilities that can be predictably encountered and
therefore exploited.

Sometimes surviving in a game should be it's own reward.


'''

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