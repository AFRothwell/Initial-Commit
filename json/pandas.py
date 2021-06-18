# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:37:18 2021

@author: Andrew Rothwell
"""

import pandas as pd

original_file = pd.read_json (r'iris.json')

print(original_file)


original_file.to_json(r'iris_new.json', orient = 'values')

edited_file = pd.read_json (r'iris_new.json')

print(edited_file)