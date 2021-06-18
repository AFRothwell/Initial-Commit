# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 11:36:28 2021

@author: Andrew Rothwell
"""

import csv

def transform_user_details(csv_file_name):
    new_user_data = []


    with open(csv_file_name, newline='\n') as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter = ",")
        
        for user in user_details_csv:
            transformation = []
            transformation.append(user[1])
            transformation.append(user[2])
            transformation.append(user[-1])
            new_user_data.append(transformation)
            
    return new_user_data

print(transform_user_details("user_details.csv")[1:])

def create_new_user_data_csv(old_user_data_file = "user_details.csv", new_file_name = 'new_user_data.csv'):
    new_user_data = transform_user_details(old_user_data_file)
    new_file = open(new_file_name, 'w')

    
    with new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_data)
        
create_new_user_data_csv()
    
# counter = 0
# for i in tranform_user_details("user_details.csv"):
#     counter += 1
#     if counter > 1:
#         print(i[1])
#     else:
#         continue