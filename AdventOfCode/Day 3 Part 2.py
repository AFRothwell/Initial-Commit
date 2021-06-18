# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 15:05:43 2021

@author: Andrew Rothwell
"""

'''

--- Part Two ---
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?

'''

input = [x[:-1] for x in open("day 3 input.txt", "r").readlines()]

forest = []
iterations = 0
answer = 1
input_list = [[3,1],[1,1],[5,1],[7,1],[1,2]]
for row in input:
    forest.append(list(row))

for i in range(len(input_list)):
    x = 0    
    y = 0


    right = input_list[iterations][0]
    down = input_list[iterations][1]
    trees = 0
    for i in (range(len(forest)//down)):
        
        if forest[y][x] == "#":
            trees += 1
            
        for i in range(right):
            x += 1
            if x > 30:
                x = 0
        for i in range(down):
            y += 1
    print(trees)
    answer *= trees
    iterations +=1
    
print(answer)