import web, pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test
posts = db.posts #posts is a collections

def get_post():
	post = posts.find()
	return post

def new_post(title, text):
    post_id = posts.insert({"title": title,  "content": text})

def del_post(title):
    posts.delete({"title": title})

def update_post(title):
    db.update('entries', where="id=$id", vars=locals(),
        title=title, content=text) 


