# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 11:11:05 2021

@author: Andrew Rothwell
"""

import csv

with open("user_details.csv", newline='\n') as csvfile:
    csvreader = csv.reader(csvfile)

    # print(list(csvreader))


    # counter = 0
    # for row in csvreader:
    #     counter += 1
    #     if counter > 0:
    #         print(row[-1])
    #     else:
    #         continue


    # for row in csvreader:
    #     print(row)


    # iterable_csv = iter(csvreader)
    # next(iterable_csv)
    # for row in iterable_csv:
    #     print(row[-1])
