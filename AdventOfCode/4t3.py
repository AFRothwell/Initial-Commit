# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 17:02:42 2021

@author: Andrew Rothwell
"""

dict_type = {"byr": "", "iyr": "","eyr": "", "hgt": "","hcl": "", "ecl": "","pid": "", "cid": ""}

text = "eyr:2028 iyr:2016 byr:1995 ecl:oth pid:543685203 hcl:#c0946f hgt:152cm cid:252"

dict_type = {"byr": "", "iyr": "","eyr": "", "hgt": "","hcl": "", "ecl": "","pid": "", "cid": ""}

text = text.split(" ")

text = [field.split(":") for field in text]

new_field = dict_type


for i in range(len(new_field)):
    new_field[text[i][0]] = text[i][1]
    
    
    
