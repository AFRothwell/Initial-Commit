# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 14:47:41 2021

@author: Andrew Rothwell
"""

from simple_calc import SimpleCalc
import unittest

class Calctests(unittest.TestCase):
    
    calc = SimpleCalc()
    
    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 8)
        
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)