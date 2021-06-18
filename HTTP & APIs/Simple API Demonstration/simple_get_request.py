# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 18:54:10 2021

@author: Andrew Rothwell
"""


import requests

# Gets a single post by id.
class GetRequests:
    
    def __init__(self, post_id = ""):
        self.post_id = post_id


    def single_id(self, post_id):
        return requests.get("https://jsonplaceholder.typicode.com/posts/" + str(post_id))
