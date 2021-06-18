# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:19:11 2021

@author: Andrew Rothwell
"""

from sci_calc import find_sqrt, find_ceil

def test_find_sqrt():
    assert find_sqrt(100) == 10.0
    
    
def test_find_ceil():
    assert find_ceil(12.7) == 13
