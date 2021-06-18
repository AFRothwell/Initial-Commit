# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 14:39:36 2021

@author: Andrew Rothwell
"""

'''

--- Day 3: Toboggan Trajectory ---
With the toboggan login problems resolved, you set off toward the airport. 
While travel by toboggan might be easy, it's certainly not safe: there's very 
minimal steering and the area is covered in trees. You'll need to see which 
angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer 
coordinates in a grid. You make a map (your puzzle input) of the open squares 
(.) and trees (#) you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
These aren't the only trees, though; due to something you read about once 
involving arboreal genetics and biome stability, the same pattern repeats to 
the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
You start on the open square (.) in the top-left corner and need to reach the 
bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper 
model that prefers rational numbers); start by counting all the trees you 
would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 
3 and down 1. Then, check the position that is right 3 and down 1 from there, 
and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where 
there was an open square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
In this example, traversing the map using this slope would cause you to 
encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 
and down 1, how many trees would you encounter?

'''

'''

So the strings I was given weren't very long which I reckon ties into the fact
that the forest is supposed to repeat. I reckon I will have to go from max to
0 at that point and continue down the list of strings.

There are 32 spaces per row. I could predict the path and then clip into the
next list as expected but I'd rather use some kind of function to predict it.

Started by getting the input split into a list of lists. Now I can try to use
indexing as a rudimentary 2D coordinate system. It will also make it much
easier to detect what is in a tile since now all tilerows are their own list
and all tiles are elements in those lists.

x = [0 to 31]

y = [0 to 323]

I'll try using itertools with a list from [0 to 31] for x to generate the x
coordinates.

Too complicated, solved it using my own iterative process instead.

'''

input = [x[:-1] for x in open("day 3 input.txt", "r").readlines()]

x = 0    
y = 0
trees = 0
forest = []

for row in input:
    forest.append(list(row))


for i in range(len(forest)):
    if forest[y][x] == "#":
        trees += 1
    for i in range(3):
        x += 1
        if x > 30:
            x = 0

    print(x)
    y += 1




