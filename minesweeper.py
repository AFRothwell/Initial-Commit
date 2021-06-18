# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 13:34:27 2021

@author: Andrew Rothwell
"""

import random as rand


minefield = [[],[],[],[],[]]

minelocations = []

for i in range(0,5):
    minelocation = [rand.randint(0,4),rand.randint(0,4)]
    while minelocation in minelocations:
        minelocation = [rand.randint(0,4),rand.randint(0,4)]
    minelocations.append([rand.randint(0,4),rand.randint(0,4)])

for x in range(0,5):
    for y in range(0,5):
        minefield[y].append("X")

minelocations[2] = [1,0]

explosion = 0

while explosion == 0:
    dig = [int(input("x: ")),int(input("y: "))]
    if dig in minelocations:
        print("KABLOOEY")
        explosion = 1
        break
    minefield[dig[0]] [dig[1]] = "O"
    
    for i in minefield:
        print(i)


