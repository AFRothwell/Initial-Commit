# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 15:48:42 2021

@author: Andrew Rothwell
"""

'''

--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers
you a starfish coin they had left over from a past vacation. They offer you a
second one if you can find three numbers in your expense report that meet the
same criteria.

Using the above example again, the three entries that sum to 2020 are 979,
366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to
2020?

Your puzzle answer was 162292410.

'''
list = [int(x) for x in open("day 1 input.txt", "r").readlines()]


index_1 = 0
index_2 = 0
index_3 = 0
number_1 = list[index_1]
number_2 = list[index_2]
number_3 = list[index_3]

for index_3 in range(len(list)):
    #iterates over the list of numbers, assigning them to number_2
    for index_2 in range(len(list)):
        #Iterates over the list of numbers, assigning them to number_1
        for index_1 in range(len(list)):
            number_1 = list[index_1]
            #Records the two numbers that correctly sum to equal 2020.
            if number_1 + number_2 + number_3 == 2020:
                answer_1 = index_1
                answer_2 = index_2 - 1
                answer_3 = index_3 - 1
        number_2 = list[index_2]
    number_3 = list[index_3]
    

print(list[answer_1]*list[answer_2]*list[answer_3])
print(list[answer_1]+list[answer_2]+list[answer_3])


'''

Personal Notes:
    
I would have liked to have read the input as html, didn't
think of doing that at the time so I'll give it a go in the future! It was
good to get back to python after SQL, it's a lot more versatile!


'''