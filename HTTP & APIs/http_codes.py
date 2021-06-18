# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 19:13:32 2021

@author: Andrew Rothwell
"""

# Had to add encoding because excel makes csv files with byte order marks...
http_codes = [x.split(",") for x in open("http_codes.csv", encoding = "utf-8-sig")]



class HTTPCodes:
    
    def __init__(self, status_code, status_class, information_url):
        status_code = self.status_code
        status_class = self.status_class
        information_url = self.information_url
        
        
    def further_info(status_code):
        return self.status_class, information_url