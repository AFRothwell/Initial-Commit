# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 14:44:27 2021

@author: Andrew Rothwell
"""

from time import sleep

player1 = "Jerry Seinfeld"

if player1 == "Jerry Seinfeld":
    bee = [x for x in open("bee.txt", "r").readlines()]
    for row in bee:
        print(row)
        sleep(0.5)