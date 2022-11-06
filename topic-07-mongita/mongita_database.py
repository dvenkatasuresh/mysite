# database.py - functions for managing database

from mongita import MongitaClientDisk
client = MongitaClientDisk()
from bson.objectid import ObjectId

shopping_db = client.shopping_db
list_collection = shopping_db.list_collection

def get_items(id=None):
    if id == None:
        items = list_collection.find({})
    else:
        items = list_collection.find({'_id':ObjectId(id)})
    items = [{'id':str(item['_id']), 'description':item['description']} for item in items]
    return items

def add_item(description):
    list_collection.insert_one({'description':description})

def delete_item(id):
    list_collection.delete_one({'_id':ObjectId(id)})

def update_item(id, description):
    list_collection.update_one({'_id':ObjectId(id)}, {'$set':{'description':description}})
