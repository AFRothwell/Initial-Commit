# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 10:21:22 2021

@author: Andrew Rothwell
"""

'''


/posts	100 posts
/comments	500 comments
/albums	100 albums
/photos	5000 photos
/todos	200 todos
/users	10 users

GET	/posts
GET	/posts/1
GET	/posts/1/comments
GET	/comments?postId=1
POST	/posts
PUT	/posts/1
PATCH	/posts/1
DELETE	/posts/1


{
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}


'''

import requests

from url_helper import UrlHelper

url = UrlHelper

# Gets a single post by id.
class GetRequests:
    
    def __init__(self, post_id = "", title = "", body = "", user_id = ""):
        self.post_id = post_id
        self.user_id = user_id
        self.title = title
        self.body = body

    def single_id(self, post_id):
        return requests.get(url.ez_url() + "posts/" + str(post_id))
    
    def single_user_id(self, user_id):
        return requests.get(url.ez_url() + "posts?userId=" + str(user_id))
    
    def body_contains_str(self, body):
        return requests.get